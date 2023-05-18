import argparse
from src.models import (
    JacquesChiracSpeechModel,
    generate_chorus,
)
from src.twitter_handler import post_tweet2


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
        jcsm = JacquesChiracSpeechModel(chorus=generate_chorus())
        print(jcsm.generate_sentence())
        # import pandas as pd
        # df = pd.read_csv("data/jacques_chirac_speech.csv", sep=";")
        # print(df.head())
        # print(post_tweet2("Ninja"))
    else:
        print("Production mode.")
