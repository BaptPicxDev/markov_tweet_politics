import argparse
from src.models import (
    JacquesChiracSpeechModel,
    generate_chorus,
)
from src.twitter_handler import post_tweet


parser = argparse.ArgumentParser(
    prog='PoetryTest',
    description='This is a poetry tutorial',
)
parser.add_argument(
    "-d",
    "--dev",
    action="store_true",
    help='Run the progam in development mode.',
)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.dev:
        # jcsm = JacquesChiracSpeechModel(chorus=generate_chorus())
        # print(jcsm.generate_sentence())
        post_tweet("Ninja")
    else:
        print("Production mode.")
