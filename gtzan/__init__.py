import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from gtzan.data.make_dataset import make_dataset_dl
from gtzan.utils import majority_voting
from gtzan.utils import get_genres
from tensorflow.keras.models import load_model 

__all__ = ['AppManager']


class AppManager:
    def __init__(self, song, genres):
        self.song = song
        self.genres = genres

    def run(self):
        
        X = make_dataset_dl(self.song)
        model = load_model("model/custom_cnn_2d.h5")
        preds = model.predict(X)
        votes = majority_voting(preds, self.genres)
        genre1 = votes[0][0]
        p1 = votes[0][1]*100
        p2="%"
        global prob1
        prob1 = str(p1) + p2
        
        # for top 3 genres:
        # genre2=votes[1][0]
        # prob2=votes[1][1]*100
        # genre3=votes[2][0]
        # prob3=votes[2][1]*100

        return genre1
        
    def prob(self):
        return prob1
