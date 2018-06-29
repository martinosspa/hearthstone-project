from keras.layers import *
import json
import os


def prepare_data():
    with open("{}\\data.json".format(os.path.split(__file__)[-2])) as f:
        #print(json.load(f))
        games = json.load(f)["games"]
        for game in games:
            game[]


if __name__ == "__main__":
    read_data()
