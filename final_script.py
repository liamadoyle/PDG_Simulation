import csv
import itertools
import os
import axelrod as axl
import numpy as np

# Set a seed for replicability
np.random.seed(42)

# Define game a (CI = .2)
A = np.array([[3, 0], [10, 1]])
B = np.array([[3, 10], [0, 1]])
gamea = axl.AsymmetricGame(A, B)

# Define game b (CI = .4)
A = np.array([[5, 0], [10, 1]])
B = np.array([[5, 10], [0, 1]])
gameb = axl.AsymmetricGame(A, B)

# Define game c (CI = .6)
A = np.array([[7, 0], [10, 1]])
B = np.array([[7, 10], [0, 1]])
gamec = axl.AsymmetricGame(A, B)

# Define game d (CI = .8)
A = np.array([[9, 0], [10, 1]])
B = np.array([[9, 10], [0, 1]])
gamed = axl.AsymmetricGame(A, B)

# Define the strategies to be played
strategies = [axl.Defector(), axl.AntiTitForTat(), axl.TrickyCooperator(), axl.TitFor2Tats(), axl.TitForTat(), axl.TwoTitsForTat()]

# Define the number of matches to play for each strategy combination
num_matches = 200

# Define the game names and their corresponding objects
games = [('gamea', gamea), ('gameb', gameb), ('gamec', gamec), ('gamed', gamed)]

# Specify the directory path where you want to save the CSV file
directory_path = r"C:\Users\lad81\Dropbox\Ph.D. Year 3\Dissertation\Study 3\Python\VSC"

# Check if the directory exists; if not, create it
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Open CSV file for writing in the specified directory
output_file = os.path.join(directory_path, 'stochastic_new2.csv')
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Game', 'Turns', 'Match_Number', 'Player1', 'Player2', 'Final_Score_Player1', 'Final_Score_Player2',
                  'Final_Score_Per_Turn_Player1', 'Final_Score_Per_Turn_Player2',
                  'Cooperation_Player1', 'Cooperation_Player2',
                  'Normalized_Cooperation_Player1', 'Normalized_Cooperation_Player2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate all combinations of strategies
    strategy_combinations = list(itertools.product(strategies, repeat=2))

    # Play matches for each combination of strategies
    for game_name, game in games:
        for player1, player2 in strategy_combinations:
            for turns in [1, 5, 10, 20]:
                    # Play 1000 matches
                    for match_number in range(1, num_matches + 1):
                        # Create a Match object with noise parameter
                        match = axl.Match((player1, player2), game=game, turns=turns, noise=0.3)

                        # Play the match
                        match.play()

                        # Extract relevant information
                        final_score = match.final_score()
                        final_score_per_turn = match.final_score_per_turn()
                        cooperation = match.cooperation()
                        normalised_cooperation = match.normalised_cooperation()

                        # Prepare data for CSV writing
                        data = {
                            'Game': game_name,
                            'Turns': turns,
                            'Match_Number': match_number,
                            'Player1': type(player1).__name__,
                            'Player2': type(player2).__name__,
                            'Final_Score_Player1': final_score[0],
                            'Final_Score_Player2': final_score[1],
                            'Final_Score_Per_Turn_Player1': final_score_per_turn[0],
                            'Final_Score_Per_Turn_Player2': final_score_per_turn[1],
                            'Cooperation_Player1': cooperation[0],
                            'Cooperation_Player2': cooperation[1],
                            'Normalized_Cooperation_Player1': normalised_cooperation[0],
                            'Normalized_Cooperation_Player2': normalised_cooperation[1]
                        }

                        # Write data to CSV file
                        writer.writerow(data)

print(f"1000 matches for each configuration saved to {output_file}")
