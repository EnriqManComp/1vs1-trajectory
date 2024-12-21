from 

direction = "diagonal"
world_dim = (100, 100)
restrictions = [10, 10, 90, 90]
steps = 5
player_dim = 2
player_pos = [20, 20]

trajectory = line(direction, world_dim, restrictions, steps, player_dim, player_pos)
print(trajectory)
