import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    # Now we can access `args.user_prompt`

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Gemini Api Key was not found, check your api key")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    # agent response buildingbootdev run 3d695968-98c9-4a91-b1e2-0ca53e8826b7
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=args.user_prompt)
    if response.usage_metadata is not None:
        prompt_tokens = response.usage_metadata.prompt_token_count
        candidate_tokens = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("Response was empty check your model/api key")

    # display the user prompt
    print(f"User prompt: {args.user_prompt}")
    # monitor token consumption
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidate_tokens}")
    # models answer
    print(f"Response: \n{response.text}")


if __name__ == "__main__":
    main()
