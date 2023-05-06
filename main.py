import argparse


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
        print("Dev mode.")
    else:
        print("Production mode.")
