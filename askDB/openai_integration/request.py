from openai import OpenAI
import json

client = OpenAI()

DEFAULT_MODEL = "gpt-4-1106-preview"


def chat_completion(user_message, content_system, model=DEFAULT_MODEL):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": content_system},
            {
                "role": "user",
                "content": user_message,
            },
        ],
        response_format={"type": "json_object"},
    )

    return json.loads(completion.choices[0].message.content)
