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
    return listt[0]
    # You can write the return function here and comment the print functions out.
    # Run the main function.
    """
    print("\nGiven song is a {} song\n".format(listt[0]))
    print("The top genres detected are are: \n")
    print("1. {} {}%".format(listt[0],listt[1])) # Listt[0] - top genre ; listt[1] - probability of top genre
    print("2. {} {}%".format(listt[2],listt[3])) # Listt[2] - 2nd most probable genre ; listt[3] - probability of 2nd most probable genre
    #print("3. {} {}%".format(listt[4],listt[5])) # Listt[4] - 3rd most probable genre ; listt[5] - probability of 3rd most probable genre

    """

if __name__ == '__main__':
    song = "data/audio.mp3"
    # Calling the main function
    main(song)
