import argparse
from src.models import (
    JacquesChiracSpeechModel,
    generate_chorus,
)


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
        jcsm = JacquesChiracSpeechModel(model_path="data/model_jcsm.json", chorus=generate_chorus())
        print(jcsm.generate_sentence())
    else:
        print("Production mode.")
