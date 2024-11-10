import random
from likelihood_calculation import calculate_match_likelihood

def monte_carlo_simulation(teams, matchups, selected_team, num_simulations=10):
    """Simulate the league outcomes using Monte Carlo simulations"""
    simulations = []

    for _ in range(num_simulations):
        simulated_teams = {team: data.copy() for team, data in teams.items()}
        for week, games in matchups.items():
            for game in games:
                team1, team2 = game
                likelihood = calculate_match_likelihood(team1, team2, week, simulated_teams)
                winner = team1 if random.random() < likelihood else team2
                loser = team1 if winner == team2 else team2
                
                # Update the simulated records
                if winner == team1:
                    simulated_teams[team1]['record'][0] += 1
                    simulated_teams[team2]['record'][1] += 1
                else:
                    simulated_teams[team2]['record'][0] += 1
                    simulated_teams[team1]['record'][1] += 1

        # Save the result of the simulation
        simulations.append(simulated_teams)

    # Calculate the probability of the selected team making the top 4
    top_4_prob = sum(1 for sim in simulations if list(sim.keys())[0] == selected_team) / num_simulations * 100

    return top_4_prob, simulations
