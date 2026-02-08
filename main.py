import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors
import argparse
from prompts import system_prompt
from functions.call_function import available_functions, call_function


def main():
    # Now we can access `args.user_prompt`

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Gemini Api Key was not found, check your api key")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # agent response
    for _ in range(20):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt, temperature=0)
            )

        except errors.ClientError as e:
            print(f"API error: {e}")
            return  # main() ends, exit code is still 0

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.usage_metadata is not None:
            prompt_tokens = response.usage_metadata.prompt_token_count
            candidate_tokens = response.usage_metadata.candidates_token_count
        else:
            raise RuntimeError("Response was empty check your model/api key")

        if args.verbose:
            # display the user prompt
            print(f"User prompt: {args.user_prompt}")
            # monitor token consumption
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {candidate_tokens}")

        if response.function_calls is not None:
            function_results = []
            for function_call in response.function_calls:
                # use function call.name and function_call.args
                # print(f"Calling function: {function_call.name}({function_call.args})")

                # use call_function
                function_call_result = call_function(function_call, verbose=args.verbose)

                # Defensive checks step by step
                # 1. Parts must exist and not be empty
                if not function_call_result.parts:
                    raise Exception("No parts in function_call_result")

                first_part = function_call_result.parts[0]

                # 2. function_response must nt be None
                if first_part.function_response is None:
                    raise Exception("No function_response in first_part")

                func_response = first_part.function_response

                # 3. response field must not be None
                if func_response.response is None:
                    raise Exception("No response in function_response")

                # Extract the actual "result" string from the dict
                result_dict = func_response.response

                # 4. Save the part for later use
                function_results.append(first_part)

                # 5. If verbose, print the response dict
                if args.verbose:
                    # assuming the key is "result" per your call_function
                    print(f"-> {result_dict['result']}")
            messages.append(
                types.Content(role="user", parts=function_results)
            )

        else:
            # models answer
            print(f"Response: \n{response.text}")
            break
    else:
        # This runs if the loop doesn't break out
        print("Max iterations reached without a final response.")
        sys.exit(1)


if __name__ == "__main__":
    main()
