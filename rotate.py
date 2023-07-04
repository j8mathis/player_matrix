import pandas as pd
import numpy as np
import random 

def get_line_up(player_count): 
    if player_count == 13:
        lineup = {
        '1': ['pitch','catch','1st','2nd','shortstop','3rd','left','center','right','bench','bench','bench','bench'],
        '2': ['bench','bench','bench','bench','right','center','shortstop','2nd','1st','pitch','catch','left','3rd'],
        '3': ['catch','pitch','2nd','bench','bench','bench','bench','center','shortstop','right','3rd','1st','left'],
        '4': ['center','left','3rd','shortstop','catch','bench','bench','bench','bench','1st','2nd','right','pitch'],
        '5': ['2nd','shortstop','center','bench','1st','catch','bench','right','3rd','bench','left','pitch', 'bench'],
        '6': ['left','pitch','1st','right','center','3rd','2nd','shortstop','bench', 'bench','bench','bench','catch']
        }
    
    elif player_count == 12:
        lineup = {
        '1': ['pitch','catch','1st','2nd','shortstop','3rd','left','center','right','bench','bench','bench'],
        '2': ['bench','bench','bench','right','center','shortstop','2nd','1st','pitch','catch','left','3rd'],
        '3': ['catch','pitch','2nd','bench','bench','right','center','shortstop','bench','3rd','1st','left'],
        '4': ['center','left','3rd','shortstop','catch','bench','bench','bench','1st','2nd','right','pitch'],
        '5': ['2nd','shortstop','center','bench','1st','catch','pitch','right','3rd','bench','left','bench'],
        '6': ['left','bench','1st','right','center','3rd','2nd','shortstop','bench','pitch','bench','catch']
        }
        
    elif player_count == 11:
        lineup = {
        '1': ['pitch','catch','1st','2nd','shortstop','3rd','left','center','right','bench','bench'],
        '2': ['bench','bench','left','right','center','shortstop','2nd','1st','pitch','catch','3rd'],
        '3': ['left','pitch','bench','bench','2nd','right','center','shortstop','catch','3rd','1st'],
        '4': ['1st','center','2nd','3rd','bench','bench','pitch','catch','shortstop','left','right'],
        '5': ['center','2nd','pitch','shortstop','1st','catch','bench','bench','3rd','right','left'],
        '6': ['right','shortstop','catch','pitch','3rd','1st','2nd','center','left','bench','bench'] 
        }

    elif player_count == 10:
        lineup = {
        '1': ['pitch','catch','1st','2nd','shortstop','3rd','left','center','right','bench'],
        '2': ['bench','left','2nd','right','center','shortstop','1st','3rd','pitch','catch'],
        '3': ['2nd','pitch','bench','shortstop','3rd','right','center','catch', 'left', '1st'],
        '4': ['left','shortstop','pitch','bench','right','1st','catch','2nd','1st','center'],
        '5': ['shortstop','center','right','catch','1st','left', 'bench','pitch','3rd','2nd'],
        '6': ['center','3rd','shortstop','left', 'pitch','catch', '1st', '2nd', 'right','bench'] 
        }

    elif player_count == 9:
        lineup = {
        '1': ['pitch', 'catch','1st', '2nd', '3rd', 'shortstop', 'left', 'center', 'right'],
        '2': ['3rd', 'left', 'right', 'center', 'shortstop', '1st', '2nd', 'pitch', 'catch'],
        '3': ['left','pitch','catch','1st','2nd','center', 'shortstop', 'left', '3rd'],
        '4': ['center','1st','2nd','3rd','right','pitch','catch','shortstop','left'],
        '5': ['shortstop','center','pitch','catch','1st','left','right','3rd','2nd'],
        '6': ['left','3rd','pitch','shortstop','center','2nd','1st','right','catch'] 
        }
    else:
        if player_count > 13:
            print("ERROR: You have too many players!")
        elif player_count < 9:
            print("ERROR: You don't have enough players!")
        lineup = {}

    return lineup

###################################
no = []

sub = []

output_csv = True
###################################

# players = ['Max', 'Grayson', 'Charlie', 'Silas', 'Tyce', 'Walter', 'Jamie', 'Edward', 'Stephen', 'Julian', 'Jack', 'Sander']
# players = ['Skip', 'Andre', 'Archer', 'Brody G', 'Brody B', 'Brystal', 'Edman', 'Greyson', 'John', 'Luke', 'Mateo', 'Mitchell', 'Torrey']
players = ['Archer', 'Brody G', 'Brystal', 'Greyson', 'John', 'Luke', 'Mateo', 'Torrey', 'Brody B', '', '']

random.shuffle(players)

for i in no:
    players.remove(i)

for i in sub:
    players.append(i)

player_count = len(players)
print("number of players:", player_count)
lineup = get_line_up(player_count)

if lineup: 
    df = pd.DataFrame(data=lineup)
    idx = 0
    df.insert(loc=idx, column='players', value=players)
    df_csv = df.to_csv(index=False)
    if output_csv:
        print(df_csv)
    else:
        print(df)

