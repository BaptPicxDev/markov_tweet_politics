import os

import pandas as pd
from markovchain.text import MarkovText
import markovify

def generate_chorus(data_path="data/jacques_chirac_quotes.csv") -> str:
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"No such file: {data_path}.")
    df = pd.read_csv(filepath_or_buffer=data_path, sep=";", usecols=["quote"])
    return "\n".join(list(df.quote))



class JacquesChiracSpeechModel:
    def __init__(self, model_path=None, chorus=None):
        if model_path:
            self.model = MarkovText.from_file(model_path)
        else:
            if not chorus:
                raise ValueError("You should provide a chorus.")
            self.model = MarkovText().data(chorus)
            self.save_model()

    def get_model(self):
        return self.model


    def save_model(self, model_path="data/model_jcsm.json"):
        self.model.save(model_path)

    def generate_sentence(self):
        return self.model(max_length=20)


def JacquesChiracSpeechModel2:
    def __init__(self, model_path=None, chorus=None):
        self.model = markovify.Text(chorus, state_size=3)
        self.compile()

    def get_model(self):
        return self.model

    def compile(self):
        self.model.compile()

    def generate_sentence(self):
        return self.model.make_short_sentence(20)
