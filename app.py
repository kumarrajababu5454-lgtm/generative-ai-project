from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    result = generate_text(prompt)

    print("\nGenerated Response:")
    print("-------------------")
    print(result)