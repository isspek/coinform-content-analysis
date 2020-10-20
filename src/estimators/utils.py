import torch
from langdetect import detect


CUDA = 'cuda'
CPU = 'cpu'


def get_device():
    return torch.device(CUDA) if torch.cuda.is_available() else torch.device(CPU)


def load_model_from_file(file_path: str) -> torch.nn.Module:
    model = torch.load(file_path, map_location=get_device())
    return model


def is_verifiable(tweet_text):
    if len(tweet_text.split(" ")) < 3:
        return False

    # if "url" in tweet_text:
    #     return False

    return True


def detect_language(tweet_text):
    return detect(tweet_text)


