import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
from gtzan.data.make_dataset import make_dataset_dl
from gtzan.utils import majority_voting
from gtzan.utils import get_genres
from tensorflow.keras.models import load_model

__all__ = ['AppManager']


class AppManager:
    def __init__(self, args, genres):
        self.args = args
        self.genres = genres

    def run(self):
        X = make_dataset_dl(self.args)
        model = load_model("..\models\custom_cnn_2d.h5")
        preds = model.predict(X)
        votes = majority_voting(preds, self.genres)
        print("{} is a {} song".format(self.args.song, votes[0][0]))
        print("most likely genres are: {}".format(votes[:3]))
