import os
import re
import pandas as pd
from markovchain.text import MarkovText
import markovify

def generate_chorus(data_paths=["data/jacques_chirac_quotes.csv", "data/jacques_chirac_speech.csv"]) -> str:
    if not all(os.path.exists(data_path) for data_path in data_paths):
        raise FileNotFoundError(f"No such file: {data_paths}.")
    df_quotes = pd.read_csv(filepath_or_buffer=data_paths[0], sep=";", usecols=["quote"])
    df_speechs = pd.read_csv(filepath_or_buffer=data_paths[1], sep=";", usecols=["speech"])
    return " ".join(list(df_quotes.quote)) + " ".join(list(df_speechs.speech))


def generate_corpus(folder_path="lyrics") -> str:
    """Reading all the files .txt from the folder.
    Assemble the data to generate a corpus.
    """
    corpus = "" 
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r") as fh:
            corpus += fh.read() + "\n"
    return corpus


def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text


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

    def generate_sentence(self, max_length=10):
        return self.model(max_length=max_length)


class JacquesChiracSpeechModel2:
    """Not working properly. More data are needed. actually ~150 sentences."""
    def __init__(self, model_path=None, chorus=None):
        self.model = markovify.Text(chorus, well_formed=True, reject_reg=' ', state_size=4)

    def get_model(self):
        return self.model

    def compile(self):
        self.model.compile()

    def generate_sentence(self):
        return self.model.make_short_sentence(50, tries=100)


if __name__ == "__main__":
    corpus = generate_corpus(folder_path="speeches")
    corpus += " "
    corpus += generate_corpus(folder_path="lyrics")
    clean_corpus = text_cleaner(corpus)
    JCS = JacquesChiracSpeechModel(chorus=clean_corpus)
    print(JCS.generate_sentence(max_length=12))