import pandas as pd
import numpy as np

df = pd.DataFrame({
        'A':list('abcdef'),
        'B':[1,2,3,4,5,6],
})

day_list = pd.to_datetime(['2015-01-02','2016-05-05','2015-08-09'])
#alternative
#day_list = pd.DatetimeIndex(['2015-01-02','2016-05-05','2015-08-09'])

df["rand_day"] = np.random.choice(day_list, size=len(df))

df1_transposed = df.T

#print(df)

data = {
    'player_1': ["pitch","bench","left","center","pitch","left"], 
    'player_2': ["catch","bench","pitch","1st","shortstop","catch"],
    'player_3': ["1st","bench","bench","3rd","center","1st"],
    'player_4': ["2nd","right","bench","2nd","right","pitch"],
    'player_5': ["shortstop","bench","bench","center","1st","shortstop"],
    'player_6': ["3rd","shortstop","bench","shortstop","catch","3rd"],
    'player_7': ["left","2nd","center","pitch","left","2nd"],
    'player_8': ["center","1st","shortstop","catch","3rd","center"],
    'player_9': ["right","pitch","left","2nd","bench","pitch"],
    'player_10':["bench","catch","3rd","1st","pitch","catch"],
    'player_11': ["bench","left","1st","1st","pitch","catch"],
    'player_12': ["bench","3rd","2nd","1st","pitch","catch"]
    }


#one = ['pitch', 'catch','1st', '2nd', 'shortstop', '3rd', 'left', 'center', 'right', 'bench', 'bench', 'bench']
#two = ['bench', 'bench', 'bench', 'right', 'center', 'shortstop', '2nd', '1st', 'pitch', 'catch', 'left', '3rd']
#three = ['left','pitch','bench','bench','bench','right','center', 'shortstop', 'left', '3rd','1st', '2nd']
four = ['center','1st','3rd','2nd','bench','bench','pitch','catch','bench','left','right','shortstop']
five = ['pitch','shortstop','center','2nd','1st','catch','bench','bench','3rd','left','right','bench']
six = ['left','catch','1st','pitch','shortstop','3rd','2nd','center','right','bench','bench','catch']



df2 = pd.DataFrame.from_dict(data, orient='index')
print(df2)
# for k,v in data.items():
#     print(k,v)