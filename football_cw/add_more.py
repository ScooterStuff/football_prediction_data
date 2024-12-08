import pandas as pd
from datetime import datetime

# Load the CSV file
input_file = 'premier_league_data.csv'   # Replace with your actual file path
output_file = 'transformed2.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(input_file)

# Convert Date to datetime object
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Initialize dictionaries to track team statistics
team_stats = {}
season_threshold = 60  # Gap in days to detect new season

# Function to reset team stats at the start of a new season
def reset_team_stats():
    return {
        'GoalsScored': 0,
        'GoalsConceded': 0,
        'Points': 0,
        'Form': ['M'] * 5,
        'WinStreak3': 0,
        'WinStreak5': 0,
        'LossStreak3': 0,
        'LossStreak5': 0,
    }

# Function to calculate win/loss streaks
def update_streaks(form):
    """Calculate win/loss streaks based on the last 5 matches."""
    win_streak_3 = int(form[:3] == ['W', 'W', 'W'])
    win_streak_5 = int(form[:5] == ['W', 'W', 'W', 'W', 'W'])
    loss_streak_3 = int(form[:3] == ['L', 'L', 'L'])
    loss_streak_5 = int(form[:5] == ['L', 'L', 'L', 'L', 'L'])
    return win_streak_3, win_streak_5, loss_streak_3, loss_streak_5

# Initialize matchweek counter
matchweek = 1
last_date = df['Date'].iloc[0]

# Create new columns for the target dataset
columns = [
    'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'Referee',
    'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'HF', 'AF', 'HY', 'AY', 'HR', 'AR',
    'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP',
    'HM1', 'HM2', 'HM3', 'HM4', 'HM5',
    'AM1', 'AM2', 'AM3', 'AM4', 'AM5',
    'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'HTFormPts', 'ATFormPts',
    'HTWinStreak3', 'HTWinStreak5', 'HTLossStreak3', 'HTLossStreak5',
    'ATWinStreak3', 'ATWinStreak5', 'ATLossStreak3', 'ATLossStreak5',
    'HTGD', 'ATGD', 'DiffPts', 'DiffFormPts'
]

transformed_data = []

# Iterate over each row in the dataset
for _, row in df.iterrows():
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']
    fthg = row['FTHG']
    ftag = row['FTAG']
    ftr = row['FTR']
    date = row['Date']

    # Detect new season if the date gap exceeds the threshold
    if (date - last_date).days > season_threshold:
        team_stats.clear()
        matchweek = 1

    # Ensure both teams have initialized stats
    if home_team not in team_stats:
        team_stats[home_team] = reset_team_stats()
    if away_team not in team_stats:
        team_stats[away_team] = reset_team_stats()

    # Get current stats
    home = team_stats[home_team]
    away = team_stats[away_team]

    # Calculate Goal Differences
    htgd = home['GoalsScored'] - home['GoalsConceded']
    atgd = away['GoalsScored'] - away['GoalsConceded']

    # Form Points Calculation
    form_points = {'W': 3, 'D': 1, 'L': 0}
    ht_form_pts = sum([form_points.get(x, 0) for x in home['Form']])
    at_form_pts = sum([form_points.get(x, 0) for x in away['Form']])

    # Update streaks
    home['WinStreak3'], home['WinStreak5'], home['LossStreak3'], home['LossStreak5'] = update_streaks(home['Form'])
    away['WinStreak3'], away['WinStreak5'], away['LossStreak3'], away['LossStreak5'] = update_streaks(away['Form'])

    # Append data to the new dataset
    transformed_data.append([
        date, home_team, away_team, fthg, ftag, ftr,
        row['HTHG'], row['HTAG'], row['HTR'], row['Referee'],
        row['HS'], row['AS'], row['HST'], row['AST'], row['HC'], row['AC'],
        row['HF'], row['AF'], row['HY'], row['AY'], row['HR'], row['AR'],
        home['GoalsScored'], away['GoalsScored'], home['GoalsConceded'], away['GoalsConceded'],
        home['Points'], away['Points'],
        *home['Form'], *away['Form'],
        matchweek, ''.join(home['Form']), ''.join(away['Form']),
        ht_form_pts, at_form_pts,
        home['WinStreak3'], home['WinStreak5'], home['LossStreak3'], home['LossStreak5'],
        away['WinStreak3'], away['WinStreak5'], away['LossStreak3'], away['LossStreak5'],
        htgd, atgd, home['Points'] - away['Points'], ht_form_pts - at_form_pts
    ])

    # Update stats after the match
    home['GoalsScored'] += fthg
    home['GoalsConceded'] += ftag
    away['GoalsScored'] += ftag
    away['GoalsConceded'] += fthg

    # Update points and form
    if ftr == 'H':
        home['Points'] += 3
        home['Form'] = (['W'] + home['Form'])[:5]
        away['Form'] = (['L'] + away['Form'])[:5]
    elif ftr == 'A':
        away['Points'] += 3
        home['Form'] = (['L'] + home['Form'])[:5]
        away['Form'] = (['W'] + away['Form'])[:5]
    else:
        home['Points'] += 1
        away['Points'] += 1
        home['Form'] = (['D'] + home['Form'])[:5]
        away['Form'] = (['D'] + away['Form'])[:5]

    # Update matchweek and last_date
    matchweek += 1
    last_date = date

# Create a new DataFrame and export to CSV
output_df = pd.DataFrame(transformed_data, columns=columns)
output_df.to_csv(output_file, index=False)
print(f"Data successfully transformed and saved to {output_file}")
