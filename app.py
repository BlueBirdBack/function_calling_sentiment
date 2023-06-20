import os
import json
import openai
import argparse
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']


def classify(user_message: str, model: str = "gpt-4-0613") -> str:
    sentiments = [
        "Joy",
        "Trust",
        "Fear",
        "Surprise",
        "Sadness",
        "Disgust",
        "Anger",
        "Anticipation",
        "Optimism",
        "Love",
        "Submission",
        "Awe",
        "Disapproval",
        "Remorse",
        "Contempt",
        "Aggression",
        "Interest",
        "Serenity",
        "Acceptance",
        "Apprehension",
        "Annoyance",
        "Distraction",
        "Boredom",
        "Skepticism",
        "Disbelief",
        "Amazement",
        "Ecstasy",
        "Admiration",
        "Terror",
        "Loathing",
        "Rage",
        "Vigilance",
        "Euphoria",
        "Envy",
        "Jealousy",
        "Panic",
        "Embarrassment",
        "Shame",
        "Guilt",
        "Pride",
        "Despair",
        "Depression",
        "Doubt",
        "Nostalgia",
        "Pity",
        "Sympathy",
        "Indifference",
        "Confusion",
        "Relief",
        "Hope",
        "Satisfaction",
        "Gratitude",
        "Humility",
        "Apathy",
        "Loneliness",
        "Overwhelm",
        "Stress",
        "Shock",
        "Disappointment",
        "Curiosity",
        "Excitement",
        "Contentment",
        "Inspiration",
        "Empathy",
        "Compassion",
        "Frustration",
        "Resentment",
        "Regret",
        "Resilience",
        "Empowerment"
    ]

    functions = [{
        "name": "print_sentiment",
        "description": "A function that prints the given sentiment",
        "parameters": {
            "type": "object",
            "properties": {
                "sentiment": {
                    "type": "string",
                    "enum": sentiments,
                    "description": "The sentiment."
                },
            },
            "required": ["sentiment"],
        }
    }]

    messages = [{"role": "user", "content": user_message}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        functions=functions,
        function_call={"name": "print_sentiment"},
        temperature=0.5
    )

    assistant_message = response.choices[0].message
    # print(assistant_message)
    function_call = assistant_message["function_call"]
    argument = json.loads(function_call["arguments"])

    return argument


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify user\'s message.')
    parser.add_argument('user_message', type=str,
                        help='User\'s message to classify')
    parser.add_argument('--model', type=str, default="gpt-4-0613",
                        help='The model to use for classification')
    args = parser.parse_args()

    print(classify(args.user_message, args.model))
