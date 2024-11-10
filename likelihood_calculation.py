# likelihood_calculation.py
from historical_data import get_historical_data

def calculate_match_likelihood(team1, team2, week, teams):
    """Calculate the likelihood of a match outcome based on historical data and team performance"""
    data = get_historical_data(week, team1, team2)
    if not data:
        return 0.5  # Default to 50% if no historical data

    points1, points2 = data
    raw_score = 0.25 * (points1 / (points1 + points2))  # Weight: 25%
    points_against = 0.25 * (teams[team1]['points_against'] / (teams[team1]['points_against'] + teams[team2]['points_against']))  # Weight: 25%
    recent_performance = 0.25 * (teams[team1]['points_scored'] / teams[team2]['points_scored'])  # Weight: 25%
    matchup_history = 0.25 * (points1 / points2)  # Weight: 25%

    # Aggregate likelihood
    return raw_score + points_against + recent_performance + matchup_history
