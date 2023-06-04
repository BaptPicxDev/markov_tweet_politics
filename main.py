import argparse
from src.models import (
    JacquesChiracSpeechModel,
    generate_chorus,
)
from src.discord_bot import DiscordBot
from src.wsgi import run_server


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
parser.add_argument(
    "-a",
    "--api",
    action="store_true",
    help="Run the api",
)
parser.add_argument(
    "-b",
    "--bot",
    action="store_true",
    help="Run the bod",
)

if __name__ == "__main__":
    args = parser.parse_args()
    if args.dev:
        jcsm = JacquesChiracSpeechModel(chorus=generate_chorus())
        print(jcsm.generate_sentence())
    elif args.api:
        run_server()
    elif args.bot:
        bot = DiscordBot()
        bot.run()
    else:
        print("Production mode.")
