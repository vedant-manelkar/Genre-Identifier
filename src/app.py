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
    listt = app.run()

    print("\nGiven song is a {} song\n".format(listt[6]))
    print("The top genres detected are are: \n")
    print("1. {} {}%".format(listt[0],listt[1]))
    print("2. {} {}%".format(listt[2],listt[3]))
    print("3. {} {}%".format(listt[4],listt[5]))

if __name__ == '__main__':
    song = "../data/iza_meu_talisma.mp3"

    # Call the main function
    main(song)
