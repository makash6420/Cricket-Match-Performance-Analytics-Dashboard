import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Akash/OneDrive/Desktop/Match_ID,Toss,Team,Player,Runs,Wick.txt')
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)
print(df)

top_run = df.groupby("Player")["Runs"].sum().sort_values(ascending=False)
print(top_run.head())

best_bowler = df.groupby("Player")["Wickets"].sum().sort_values(ascending=False)
print(best_bowler.head())

wins = df[df["Match_Results"] == "Win"]

winning_percentage = (
    wins.groupby("Team").size() /
    df.groupby("Team").size()
) * 100

print(winning_percentage)

home = df[df["Home_Away"] == "Home"]
away = df[df["Home_Away"] == "Away"]

print(home.groupby("Team")["Runs"].mean())
print(away.groupby("Team")["Runs"].mean())

toss_win_matches = df[(df['Toss'] == df['Team']) &
                      (df['Match_Results'] == 'Win')]

total_toss_wins = df['Toss'].nunique()
toss_impact_percentage = (
    len(toss_win_matches) / len(df[df['Team'] == df['Toss']])
) * 100
print("Toss Impact Percentage:", round(toss_impact_percentage, 2), "%")

venue_analysis = (
    df[(df['Match_Results'] == 'Win') &
       (df['Toss_Decision'] == 'Bowl')]
    .groupby('Venue')
    .size()
    .sort_values(ascending=False)
)
print(venue_analysis)

toss_decision_analysis = (
    df[df['Match_Results'] == 'Win']
    .groupby('Toss_Decision')
    .size()
)

toss_decision_analysis.plot(
    kind='bar',
    figsize=(6,4)
)

plt.title("Wins by Toss Decision")
plt.xlabel("Toss Decision")
plt.ylabel("Number of Wins")
plt.show()


top_players = (
    df.groupby('Player')['Runs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
top_players.plot(kind='bar')

plt.title('Top 10 Run Scorers')
plt.xlabel('Player')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

team_runs = df.groupby('Team')['Runs'].sum()

plt.figure(figsize=(10,6))
team_runs.plot(kind='line', marker='o')

plt.title('Team Performance Analysis')
plt.xlabel('Team')
plt.ylabel('Total Runs')
plt.grid(True)
plt.tight_layout()

plt.show()

