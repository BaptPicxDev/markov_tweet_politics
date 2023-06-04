import os

import pandas as pd
from markovchain.text import MarkovText
import markovify

def generate_chorus(data_paths=["data/jacques_chirac_quotes.csv", "data/jacques_chirac_speech.csv"]) -> str:
    if not all(os.path.exists(data_path) for data_path in data_paths):
        raise FileNotFoundError(f"No such file: {data_paths}.")
    df_quotes = pd.read_csv(filepath_or_buffer=data_paths[0], sep=";", usecols=["quote"])
    df_speechs = pd.read_csv(filepath_or_buffer=data_paths[1], sep=";", usecols=["speech"])
    return " ".join(list(df_quotes.quote)) + " ".join(list(df_speechs.speech))



class JacquesChiracSpeechModel:
    def __init__(self, model_path=None, chorus=None):
        if model_path:
            self.model = MarkovText.from_file(model_path)
        else:
            if not chorus:
                raise ValueError("You should provide a chorus.")
            self.model = MarkovText()
            self.model.data(chorus)
            self.save_model()

    def get_model(self):
        return self.model

    def save_model(self, model_path="data/model_jcsm.json"):
        self.model.save(model_path)

    def generate_sentence(self):
        return self.model(max_length=20)


class JacquesChiracSpeechModel2:
    """Not working properly. More data are needed. actually ~150 sentences."""
    def __init__(self, model_path=None, chorus=None):
        self.model = markovify.Text(" ".join(chorus)[0], well_formed=True, reject_reg=' ', state_size=4)

    def get_model(self):
        return self.model

    def compile(self):
        self.model.compile()

    def generate_sentence(self):
        return self.model.make_short_sentence(50, tries=100)


if __name__ == "__main__":
    model = JacquesChiracSpeechModel2(chorus=generate_chorus())
    generated_sentence = model.generate_sentence()
    print(generated_sentence)
