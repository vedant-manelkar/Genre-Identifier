import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from gtzan import AppManager
# Constants
genres = {
    'Metal': 0, 'Disco': 1, 'Classical': 2, 'Hiphop': 3, 'Jazz': 4,
    'Country': 5, 'Pop': 6, 'Blues': 7, 'Reggae': 8, 'Rock': 9
}

# @RUN: Main function to call the appmanager
def main(song):

    app = AppManager(song, genres)
    genree = app.run()

    global prob1
    prob1=app.prob()

    return genree 

def probability(song):

    return prob1

if __name__ == '__main__':
    song = "data/audio.mp3"
    
    # Calling the main function for genre and probability for probability
    main(song)
    probability(song)
