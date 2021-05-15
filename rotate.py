import pandas as pd
import numpy as np
import random


def get_line_up(player_count):
    if player_count == 12:
        lineup = {
            "1": [
                "pitch",
                "catch",
                "1st",
                "2nd",
                "shortstop",
                "3rd",
                "left",
                "center",
                "right",
                "bench",
                "bench",
                "bench",
            ],
            "2": [
                "bench",
                "bench",
                "bench",
                "right",
                "center",
                "shortstop",
                "2nd",
                "1st",
                "pitch",
                "catch",
                "left",
                "3rd",
            ],
            "3": [
                "left",
                "pitch",
                "bench",
                "bench",
                "bench",
                "right",
                "center",
                "shortstop",
                "left",
                "3rd",
                "1st",
                "2nd",
            ],
            "4": [
                "center",
                "1st",
                "3rd",
                "2nd",
                "bench",
                "bench",
                "pitch",
                "catch",
                "bench",
                "left",
                "right",
                "shortstop",
            ],
            "5": [
                "pitch",
                "shortstop",
                "center",
                "2nd",
                "1st",
                "catch",
                "bench",
                "bench",
                "3rd",
                "left",
                "right",
                "bench",
            ],
            "6": [
                "left",
                "catch",
                "1st",
                "pitch",
                "shortstop",
                "3rd",
                "2nd",
                "center",
                "right",
                "bench",
                "bench",
                "catch",
            ],
        }

    elif player_count == 11:
        lineup = {
            "1": [
                "pitch",
                "catch",
                "1st",
                "2nd",
                "shortstop",
                "3rd",
                "left",
                "center",
                "right",
                "bench",
                "bench",
            ],
            "2": [
                "bench",
                "bench",
                "3rd",
                "right",
                "center",
                "shortstop",
                "2nd",
                "1st",
                "pitch",
                "catch",
                "left",
            ],
            "3": [
                "left",
                "pitch",
                "bench",
                "bench",
                "2nd",
                "right",
                "center",
                "shortstop",
                "left",
                "3rd",
                "1st",
            ],
            "4": [
                "center",
                "1st",
                "3rd",
                "2nd",
                "bench",
                "bench",
                "pitch",
                "catch",
                "shortstop",
                "left",
                "right",
            ],
            "5": [
                "pitch",
                "shortstop",
                "center",
                "2nd",
                "1st",
                "catch",
                "bench",
                "bench",
                "3rd",
                "left",
                "right",
            ],
            "6": [
                "left",
                "catch",
                "1st",
                "pitch",
                "shortstop",
                "3rd",
                "2nd",
                "center",
                "right",
                "bench",
                "catch",
            ],
        }

    elif player_count == 10:
        lineup = {
            "1": [
                "pitch",
                "catch",
                "1st",
                "2nd",
                "shortstop",
                "3rd",
                "left",
                "center",
                "right",
                "bench",
            ],
            "2": [
                "bench",
                "left",
                "3rd",
                "right",
                "center",
                "shortstop",
                "1st",
                "2nd",
                "pitch",
                "catch",
            ],
            "3": [
                "2nd",
                "pitch",
                "bench",
                "shortstop",
                "1st",
                "right",
                "center",
                "catch",
                "left",
                "3rd",
            ],
            "4": [
                "2nd",
                "bench",
                "left",
                "3rd",
                "right",
                "pitch",
                "catch",
                "shortstop",
                "1st",
                "center",
            ],
            "5": [
                "shortstop",
                "center",
                "pitch",
                "catch",
                "1st",
                "left",
                "bench",
                "right",
                "3rd",
                "2nd",
            ],
            "6": [
                "left",
                "3rd",
                "pitch",
                "shortstop",
                "center",
                "2nd",
                "1st",
                "right",
                "catch",
                "bench",
            ],
        }

    elif player_count == 9:
        lineup = {
            "1": [
                "pitch",
                "catch",
                "1st",
                "2nd",
                "3rd",
                "shortstop",
                "left",
                "center",
                "right",
            ],
            "2": [
                "3rd",
                "left",
                "right",
                "center",
                "shortstop",
                "1st",
                "2nd",
                "pitch",
                "catch",
            ],
            "3": [
                "left",
                "pitch",
                "catch",
                "1st",
                "2nd",
                "center",
                "shortstop",
                "left",
                "3rd",
            ],
            "4": [
                "center",
                "1st",
                "2nd",
                "3rd",
                "right",
                "pitch",
                "catch",
                "shortstop",
                "left",
            ],
            "5": [
                "shortstop",
                "center",
                "pitch",
                "catch",
                "1st",
                "left",
                "right",
                "3rd",
                "2nd",
            ],
            "6": [
                "left",
                "3rd",
                "pitch",
                "shortstop",
                "center",
                "2nd",
                "1st",
                "right",
                "catch",
            ],
        }
    else:
        if player_count > 12:
            print("ERROR: You have too many players!")
        elif player_count < 9:
            print("ERROR: You don't have enough players!")
        lineup = {}

    return lineup


###################################
no = ["Edward", "Julian"]

sub = []

output_csv = False
###################################

players = [
    "Max",
    "Grayson",
    "Charlie",
    "Silas",
    "Tyce",
    "Walter",
    "Jamie",
    "Edward",
    "Stephen",
    "Julian",
    "Jack",
    "Sander",
]
random.shuffle(players)

for i in no:
    players.remove(i)

for i in sub:
    players.append(i)

player_count = len(players)

lineup = get_line_up(player_count)

if lineup:
    df = pd.DataFrame(data=lineup)
    idx = 0
    df.insert(loc=idx, column="players", value=players)
    df_csv = df.to_csv(index=False)
    if output_csv:
        print(df_csv)
    else:
        print(df)
