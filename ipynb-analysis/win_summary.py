import pandas as pd
games = {}
df = pd.read_csv('college_fb_data\\cfbstats-com-2013-1-5-20\\team-game-statistics.csv')
for game in set(df['Game Code']):
    x = df[df['Game Code'] == game]
    team1 = x.head(1)
    team2 = x.tail(1)
    won = -1
    if team1['Points'].values > team2['Points'].values:
        won = 0
    else:
        won = 1
    games[str(game)] = [int(team1['Team Code']), int(team2['Team Code']), won]

print(games)
ids = list(df['Team Code'])
print(ids)
