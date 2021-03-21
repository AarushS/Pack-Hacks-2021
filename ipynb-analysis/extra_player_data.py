import pandas as pd
import pickle
player_profiles = {}
def updateProfile(csv_file, year):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        code = str(row['Player Code'])
        if code not in player_profiles.keys():
            player_profiles[code] = {'games': 1, 'year':year,
             'rush yards': row['Rush Yard'],
             'pass yards': row['Pass Yard'],
             'rush att': row['Rush Att'],
             'rush td': row['Rush TD'],
             'pass att': row['Pass Att'],
             'pass comp': row['Pass Comp'],
             'pass td':row['Pass TD'],
             'pass int': row['Pass Int']}
        elif player_profiles[code]['year'] == year:

            games = player_profiles[code]['games']
            player_profiles[code]['rush yards'] = (row['Rush Yard'] + games * player_profiles[code]['rush yards']) / (games+1) 
            player_profiles[code]['pass yards'] = (row['Pass Yard'] + games * player_profiles[code]['pass yards']) / (games+1)
            player_profiles[code]['rush att'] = (row['Rush Att'] + games * player_profiles[code]['rush att']) / (games+1)
            player_profiles[code]['rush td'] = (row['Rush TD'] + games * player_profiles[code]['rush td']) / (games+1)
            player_profiles[code]['pass att'] = (row['Pass Att'] + games * player_profiles[code]['pass att']) / (games+1)
            player_profiles[code]['pass comp'] = (row['Pass Comp'] + games * player_profiles[code]['pass comp']) / (games+1)
            player_profiles[code]['pass td'] = (row['Pass TD'] + games * player_profiles[code]['pass td']) / (games+1)
            player_profiles[code]['pass int'] = (row['Pass Int'] + games * player_profiles[code]['pass int']) / (games+1)
            player_profiles[code]['games'] += 1
            print(index, year)

updateProfile('college_fb_data/cfbstats-com-2013-1-5-20/player-game-statistics.csv', 2013)
updateProfile('college_fb_data/cfbstats-com-2012-1-5-4/player-game-statistics.csv', 2012)
updateProfile('college_fb_data/cfbstats-com-2011-1-5-0/player-game-statistics.csv', 2011)
updateProfile('college_fb_data/cfbstats-com-2010-1-5-0/player-game-statistics.csv', 2010)
updateProfile('college_fb_data/cfbstats-com-2009-1-5-0/player-game-statistics.csv', 2009)
updateProfile('college_fb_data/cfbstats-com-2008-1-5-0/player-game-statistics.csv', 2008)
updateProfile('college_fb_data/cfbstats-com-2007-1-5-0/player-game-statistics.csv', 2007)
updateProfile('college_fb_data/cfbstats-com-2006-1-5-0/player-game-statistics.csv', 2006)
updateProfile('college_fb_data/cfbstats-com-2005-1-5-0/player-game-statistics.csv', 2005)

csv_columns = ['games', 'year', 'rush yards',
             'pass yards',
             'rush att',
             'rush td',
             'pass att',
             'pass comp',
             'pass td',
             'pass int']
print(player_profiles)
print(len(player_profiles))
with open('player.pkl', 'wb') as handle:
    pickle.dump(player_profiles, handle, protocol=pickle.HIGHEST_PROTOCOL)
# x = pd.Dataframe.from_dict(player_profiles)
# x.to_csv('player_summary.csv')
