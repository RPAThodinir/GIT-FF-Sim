import random
from monte_carlo import monte_carlo_simulation
from likelihood_calculation import calculate_match_likelihood

#####

import random
from monte_carlo import monte_carlo_simulation
from likelihood_calculation import calculate_match_likelihood

def simulate_weekly_results(teams, matchups, selected_team):
    """Run the simulation and generate results"""
    
    # Open file for the main simulation path
    with open(f"C:\\Users\\spier\\OneDrive\\Desktop\\FF Sim\\SIM RESULTS\\{selected_team}_simulation_results.txt", "w") as file:
        file.write(f"Team Investigated: {selected_team}\n")
        
        # Run Monte Carlo simulation to get path likelihood and simulations
        path_likelihood, simulations = monte_carlo_simulation(teams, matchups, selected_team)
        file.write(f"Path Likelihood: {path_likelihood:.2f}%\n\n")

        # Simulate each week's matchups for the most likely path
        possible_path_found = False
        
        # Reset teams' records at the beginning of the path
        simulated_teams = {team: data.copy() for team, data in teams.items()}
        
        for week, games in matchups.items():
            file.write(f"Week {week} Results:\n")
            for game in games:
                team1, team2 = game
                # Reset teams' records for this simulation
                simulated_teams = {team: data.copy() for team, data in teams.items()}
                
                # Calculate the likelihood of the matchup outcome
                likelihood = calculate_match_likelihood(team1, team2, week, simulated_teams)
                
                # Select the winner based on the likelihood
                winner = team1 if random.random() < likelihood else team2
                loser = team1 if winner == team2 else team2
                
                # Update teams' records based on the winner and loser (only for this specific simulation)
                if winner == team1:
                    simulated_teams[team1]['record'][0] += 1  # Win for team1
                    simulated_teams[team2]['record'][1] += 1  # Loss for team2
                else:
                    simulated_teams[team2]['record'][0] += 1  # Win for team2
                    simulated_teams[team1]['record'][1] += 1  # Loss for team1

                # Write match details to the file
                file.write(f"Matchup: {team1} vs {team2}\n")
                file.write(f"Winner: {winner}\n")
                file.write(f"Winner's Updated Record: {simulated_teams[winner]['record'][0]}-{simulated_teams[winner]['record'][1]}-{simulated_teams[winner]['record'][2]}\n")
                file.write(f"Loser: {loser}\n")
                file.write(f"Loser's Updated Record: {simulated_teams[loser]['record'][0]}-{simulated_teams[loser]['record'][1]}-{simulated_teams[loser]['record'][2]}\n\n")

            # After each week, calculate top 4 teams (only this single path)
            sorted_teams = sorted(simulated_teams.items(), key=lambda item: (item[1]['record'][0], item[1]['points_scored']), reverse=True)
            file.write(f"Top 4 Teams After Week {week}:\n")
            for rank, (team, data) in enumerate(sorted_teams[:4], 1):
                file.write(f"{rank}. {team}: {data['record'][0]}-{data['record'][1]}-{data['record'][2]}\n")
            file.write("\n")

        # Final standings after all weeks (showing results of the most likely path)
        sorted_teams = sorted(simulated_teams.items(), key=lambda item: (item[1]['record'][0], item[1]['points_scored']), reverse=True)
        file.write("Final Standings After Week 15:\n")
        for rank, (team, data) in enumerate(sorted_teams, 1):
            file.write(f"{rank}. {team}: {data['record'][0]}-{data['record'][1]}-{data['record'][2]}\n")
        
    # Save the Monte Carlo Simulation Results in a separate file
    with open(f"C:\\Users\\spier\\OneDrive\\Desktop\\FF Sim\\SIM RESULTS\\{selected_team}_sim_details.txt", "w") as sim_details_file:
        sim_details_file.write(f"Monte Carlo Simulation Results for {selected_team}\n")
        sim_details_file.write(f"Path Likelihood: {path_likelihood:.2f}%\n\n")
        
        # Simulate multiple times and write results to file
        for sim in simulations:
            sim_details_file.write(f"Simulated Standings: {sim}\n")
        
        sim_details_file.write("\nMonte Carlo Simulated Final Standings:\n")
        # Flatten the simulation results into a list of teams with records
        all_sim_teams = []
        for sim in simulations:
            for team, data in sim.items():
                all_sim_teams.append((team, data))

        # Sort the teams based on their records
        sorted_sim_teams = sorted(all_sim_teams, key=lambda team_data: team_data[1]['record'][0], reverse=True)
        for rank, (team, data) in enumerate(sorted_sim_teams[:4], 1):
            sim_details_file.write(f"{rank}. {team}: {data['record'][0]}-{data['record'][1]}-{data['record'][2]}\n")


######

# Select the team (set to Fantasy Wizard)
selected_team = "The Team With No Name"  # You can change this to any team you'd like to simulate

# Team data (teams and matchups should be defined elsewhere, provided earlier)
teams = {
    "Steamrollers": {'record': [8, 1, 0], 'points_scored': 1048.04, 'points_against': 873.16},
    "Thor's Glass Hammer": {'record': [7, 2, 0], 'points_scored': 952.5, 'points_against': 861.82},
    "The Team With No Name": {'record': [5, 4, 0], 'points_scored': 1048.68, 'points_against': 968.56},
    "The Gibbly Plumps": {'record': [5, 4, 0], 'points_scored': 888.62, 'points_against': 931.6},
    "Nightmare Tornado Supernova": {'record': [4, 5, 0], 'points_scored': 1072.44, 'points_against': 1059.22},
    "Michael's Majestic Team": {'record': [4, 5, 0], 'points_scored': 1027.66, 'points_against': 1020.34},
    "Ken's Impressive Team": {'record': [4, 5, 0], 'points_scored': 883.44, 'points_against': 906.12},
    "Teddy's Terrific Team": {'record': [3, 6, 0], 'points_scored': 1005.06, 'points_against': 1018.42},
    "Fantasy Wizard": {'record': [3, 6, 0], 'points_scored': 869.42, 'points_against': 1016.1},
    "The Happy Pancakes": {'record': [2, 7, 0], 'points_scored': 904.18, 'points_against': 1044.7}
}

# Matchup data for weeks 10 to 15 (same structure as earlier)
matchups = {
    10: [
        ("The Team With No Name", "Michael's Majestic Team"),
        ("Fantasy Wizard", "The Gibbly Plumps"),
        ("Teddy's Terrific Team", "Nightmare Tornado Supernova"),
        ("Steamrollers", "The Happy Pancakes"),
        ("Thor's Glass Hammer", "Ken's Impressive Team")
    ],
    11: [
        ("The Team With No Name", "The Gibbly Plumps"),
        ("Fantasy Wizard", "Nightmare Tornado Supernova"),
        ("Teddy's Terrific Team", "Steamrollers"),
        ("Thor's Glass Hammer", "The Happy Pancakes"),
        ("Ken's Impressive Team", "Michael's Majestic Team")
    ],
    12: [
        ("The Team With No Name", "Nightmare Tornado Supernova"),
        ("Fantasy Wizard", "Steamrollers"),
        ("Teddy's Terrific Team", "The Happy Pancakes"),
        ("Thor's Glass Hammer", "Michael's Majestic Team"),
        ("The Gibbly Plumps", "Ken's Impressive Team")
    ],
    13: [
        ("The Team With No Name", "Steamrollers"),
        ("Fantasy Wizard", "The Happy Pancakes"),
        ("Teddy's Terrific Team", "Thor's Glass Hammer"),
        ("Nightmare Tornado Supernova", "Ken's Impressive Team"),
        ("The Gibbly Plumps", "Michael's Majestic Team")
    ],
    14: [
        ("The Team With No Name", "The Happy Pancakes"),
        ("Fantasy Wizard", "Teddy's Terrific Team"),
        ("Steamrollers", "Ken's Impressive Team"),
        ("Thor's Glass Hammer", "The Gibbly Plumps"),
        ("Nightmare Tornado Supernova", "Michael's Majestic Team")
    ],
    15: [
        ("The Team With No Name", "Teddy's Terrific Team"),
        ("Fantasy Wizard", "Thor's Glass Hammer"),
        ("Steamrollers", "Michael's Majestic Team"),
        ("Nightmare Tornado Supernova", "The Gibbly Plumps"),
        ("The Happy Pancakes", "Ken's Impressive Team")
    ]
}

# Run the simulation for the selected team
simulate_weekly_results(teams, matchups, selected_team)
