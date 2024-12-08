import pandas as pd
import numpy as np

class ELOCalculator:
    def __init__(self, initial_rating=1500, k_factor=32, home_advantage=100):
        self.initial_rating = initial_rating
        self.k_factor = k_factor
        self.home_advantage = home_advantage
        self.team_ratings = {}
        
    def calculate_expected_score(self, rating_a, rating_b):
        """Calculate expected score using ELO formula"""
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    
    def get_actual_score(self, home_goals, away_goals):
        """Convert goals into actual score (1 for win, 0.5 for draw, 0 for loss)"""
        if home_goals > away_goals:
            return 1.0
        elif home_goals == away_goals:
            return 0.5
        else:
            return 0.0
    
    def safe_numeric(self, value, default=0):
        """Safely convert value to float"""
        try:
            if pd.isna(value):
                return default
            return float(value)
        except (ValueError, TypeError):
            return default
    
    def calculate_performance_multiplier(self, row):
        """Calculate performance multiplier based on match statistics"""
        # Safely convert goals to float
        home_goals = self.safe_numeric(row['FTHG'])
        away_goals = self.safe_numeric(row['FTAG'])
        
        # Basic goal difference multiplier
        goal_diff = abs(home_goals - away_goals)
        multiplier = 1.0
        
        if goal_diff == 2:
            multiplier = 1.2
        elif goal_diff == 3:
            multiplier = 1.4
        elif goal_diff >= 4:
            multiplier = 1.6
        
        # Safely convert shots on target to float
        hst = self.safe_numeric(row['HST'])
        ast = self.safe_numeric(row['AST'])
        
        # Additional multiplier based on shots on target ratio
        total_shots = hst + ast
        if total_shots > 0:
            dominant_shots = max(hst / total_shots, ast / total_shots)
            multiplier *= (1 + (dominant_shots - 0.5) * 0.2)
        
        return multiplier
    
    def process_match(self, row):
        """Process a single match and update ratings"""
        home_team = str(row['HomeTeam'])
        away_team = str(row['AwayTeam'])
        
        # Safely convert goals to float
        home_goals = self.safe_numeric(row['FTHG'])
        away_goals = self.safe_numeric(row['FTAG'])
        
        # Get or initialize ratings
        home_rating = self.team_ratings.get(home_team, self.initial_rating)
        away_rating = self.team_ratings.get(away_team, self.initial_rating)
        
        # Store original ratings
        original_home_rating = home_rating
        original_away_rating = away_rating
        
        # Add home advantage
        home_rating_with_advantage = home_rating + self.home_advantage
        
        # Calculate expected scores
        home_expected = self.calculate_expected_score(home_rating_with_advantage, away_rating)
        away_expected = 1 - home_expected
        
        # Get actual score
        home_actual = self.get_actual_score(home_goals, away_goals)
        away_actual = 1 - home_actual
        
        # Calculate performance multiplier
        performance_multiplier = self.calculate_performance_multiplier(row)
        k_factor_adjusted = self.k_factor * performance_multiplier
        
        # Update ratings
        home_rating_change = k_factor_adjusted * (home_actual - home_expected)
        away_rating_change = k_factor_adjusted * (away_actual - away_expected)
        
        self.team_ratings[home_team] = home_rating + home_rating_change
        self.team_ratings[away_team] = away_rating + away_rating_change
        
        return {
            'Date': row['Date'],
            'HomeTeam': home_team,
            'AwayTeam': away_team,
            'FTHG': home_goals,
            'FTAG': away_goals,
            'HST': self.safe_numeric(row['HST']),
            'AST': self.safe_numeric(row['AST']),
            'HomeRatingBefore': original_home_rating,
            'AwayRatingBefore': original_away_rating,
            'HomeRatingAfter': self.team_ratings[home_team],
            'AwayRatingAfter': self.team_ratings[away_team],
            'HomeRatingChange': home_rating_change,
            'AwayRatingChange': away_rating_change,
            'HomeExpectedScore': home_expected,
            'AwayExpectedScore': away_expected,
            'HomeActualScore': home_actual,
            'PerformanceMultiplier': performance_multiplier,
            'Referee': str(row['Referee'])
        }

def process_premier_league_data(file_path):
    """Process Premier League CSV data and calculate ELO ratings"""
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Initialize ELO calculator
    elo = ELOCalculator()
    results = []
    
    # Process each match
    for _, row in df.iterrows():
        result = elo.process_match(row)
        results.append(result)
    
    # Create results dataframe
    results_df = pd.DataFrame(results)
    
    # Calculate final team ratings
    final_ratings = pd.DataFrame(list(elo.team_ratings.items()), 
                               columns=['Team', 'Rating']).sort_values('Rating', ascending=False)
    
    return results_df, final_ratings

if __name__ == "__main__":
    # Replace with your actual file path
    file_path = 'premier_league_data.csv'
    
    results_df, final_ratings = process_premier_league_data(file_path)
    
    print("\nELO Rating Changes:")
    print(results_df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 
                     'HomeRatingBefore', 'HomeRatingAfter', 'HomeRatingChange',
                     'AwayRatingBefore', 'AwayRatingAfter', 'AwayRatingChange',
                     'PerformanceMultiplier']].round(2))
    
    print("\nFinal Team Ratings:")
    print(final_ratings.round(2))