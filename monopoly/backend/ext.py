
import random

class Player:
    def __init__(self, player_id, icon, cash):
        self.id = player_id
        self.icon = icon
        self.cash = cash

def distribute_into_teams(names, num_teams):
    
    teams = [[] for _ in range(num_teams)]
    for i, name in enumerate(names):
        teams[i % num_teams].append(name)
    return teams

# Example usage
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
num_teams = len(names)//2
teams = distribute_into_teams(names, num_teams)
for i, team in enumerate(teams):
    print(f"Team {i+1}: {team}")