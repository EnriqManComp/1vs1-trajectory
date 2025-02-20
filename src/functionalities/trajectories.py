import numpy as np
import copy
import matplotlib.pyplot as plt
from scipy import signal

def line(direction, restrictions, steps, player_dim, player_pos, traj_dist, player_dist):
    """
        Generate a line trajectory for the players
        Args:
            direction: str, direction of the line
            world_dim: tuple, (width, height)
            restrictions: list, limits for the player (left, up, right, down)
            steps: int, number of steps that the player will take
            player_dim: int, player dimension
            player_pos: list, player position
            traj_dist: int, minimum distance trajectory requirement
            player_dist: int, minimum distance between the players
        Returns:
            trajectory: list, list of positions for the player
    """
    trajectory = []

    # Initial position
    x, y = player_pos    

    # Final position
    x_f = copy.deepcopy(x)
    y_f = copy.deepcopy(y)

    while True:   
        if direction == "horizontal":
            if abs(x_f - x) < traj_dist:
                x_f = np.random.randint(restrictions[0] + player_dim, restrictions[2] - player_dim)
            else:
                break
        elif direction == "vertical":
            if abs(y_f - y) < traj_dist:
                y_f = np.random.randint(restrictions[1] + player_dim, restrictions[3] - player_dim)
            else:
                break        
    
    # Discretize the line using linear interpolation
    num_steps = max(abs(x_f - x), abs(y_f - y)) // steps

    for i in range(num_steps + 1):
        t = i / num_steps
        x_t = int(x + t * (x_f - x))
        y_t = int(y + t * (y_f - y))
        trajectory.append([x_t, y_t])

    # Create a trajectory for the second player

    p_trajectory = copy.deepcopy(trajectory)

    for i in range(len(p_trajectory)):
        if y + player_dist > restrictions[2]:
            p_trajectory[i][1] -= player_dist
        else:
            p_trajectory[i][1] += player_dist

    return trajectory, p_trajectory

def square(restrictions, steps, player_dim, player_pos, p_dist=20):
    """
    Generate a square trajectory for the player.
    Args:
        restrictions: tuple, (width, height)
        steps: int, number of steps that the player will take
        player_dim: int, player dimension
        player_pos: list, player position
    Returns:
        trajectory: list, list of positions for the player
    """
    trajectory = []
    p_trajectory = []

    # Initial position
    x, y = player_pos
    x_p, y_p = copy.deepcopy(x), copy.deepcopy(y)
    y_p += p_dist

    # Final position
    x_f = copy.deepcopy(x)
    y_f = copy.deepcopy(y)

    x_f_p = copy.deepcopy(x_p)
    y_f_p = copy.deepcopy(y_p)

    # Discretize the square using linear interpolation
    for i in range(4):
        
        if i == 0:
            # Final position (top left corner)
            x_f = restrictions[0] + player_dim
            y_f = restrictions[1] + player_dim
            
            x_f_p = restrictions[0] + player_dim + p_dist
            y_f_p = restrictions[1] + player_dim + p_dist

        elif i == 1:
            # Final position (bottom left corner)            
            x_f = restrictions[0] + player_dim
            y_f = restrictions[3] - player_dim
            x_f_p = restrictions[0] + player_dim + p_dist
            y_f_p = restrictions[3] - player_dim - p_dist

        elif i == 2:
            # Final position (bottom right corner)
            x_f = restrictions[2] - player_dim
            y_f = restrictions[3] - player_dim
            x_f_p = restrictions[2] - player_dim - p_dist
            y_f_p = restrictions[3] - player_dim - p_dist
        elif i == 3:
            # Final position (top right corner)
            x_f = restrictions[2] - player_dim
            y_f = restrictions[1] + player_dim
            x_f_p = restrictions[2] - player_dim - p_dist
            y_f_p = restrictions[1] + player_dim + p_dist

        num_steps = max(abs(x_f - x), abs(y_f - y)) // steps

        for j in range(num_steps + 1):
            t = j / num_steps
            x_t = int(x + t * (x_f - x))
            y_t = int(y + t * (y_f - y))
            trajectory.append([x_t, y_t])

            x_t = int(x_p + t * (x_f_p - x_p))
            y_t = int(y_p + t * (y_f_p - y_p))
            p_trajectory.append([x_t, y_t])
            

        x = copy.deepcopy(x_f)
        y = copy.deepcopy(y_f)

        x_p = copy.deepcopy(x_f_p)
        y_p = copy.deepcopy(y_f_p)

        

    return trajectory, p_trajectory


def circle(restrictions, steps, player_pos, radius, p_radius):
    """
        Generate a circle trajectory for the player
        Args:
            world_dim: tuple, (width, height)
            steps: int, number of steps that the player will take
            player_dim: int, player dimension
            player_pos: list, player position
            radius: int, radius of the circle
        Returns:
            trajectory: list, list of positions for the player
    """

    # Validate inputs
    if radius <= 0 or steps <= 0:
        raise ValueError("Radius and steps must be positive integers.")

    trajectory = []
    p_trajectory = []

    # Circle parameters
    center = [restrictions[0] // 2, restrictions[1] // 2]

    # Discretize the circle using parametric equations
    for i in range(0, 360, steps):
        angle = np.radians(i)
        x_t = int(center[0] + radius * np.cos(angle))
        y_t = int(center[1] + radius * np.sin(angle))
        trajectory.append([x_t, y_t])

        x_t = int(center[0] + p_radius * np.cos(angle))
        y_t = int(center[1] + p_radius * np.sin(angle))
        p_trajectory.append([x_t, y_t])   

    return trajectory, p_trajectory

def sawtooth(restrictions, angle, steps, player_dim, player_pos, traj_dist, p_dist):
    
    trajectory = []
    p_trajectory = []

    # Initial position
    x, y = player_pos

    # Final position
    x_f = copy.deepcopy(x)

    y_f_points = []
    x_f_points = []

    while True:   
        if abs(x_f - x) < traj_dist:
            x_f = np.random.randint(restrictions[0] + player_dim, restrictions[2] - player_dim)
        else:
            break

    y_f = copy.deepcopy(y)

    # Sawtooth trajectory

    # First triangle

    h = (abs(x - x_f) // 4) * np.tan(np.radians(angle))
    y_f_1 = y_f + h
    x_f_1 = x + (abs(x - x_f) // 4)

    # Discretize the line using linear interpolation
    num_steps = max(abs(x_f_1 - x), abs(y_f_1 - y)) // steps

    for i in range(int(num_steps + 1)):
        t = i / num_steps
        x_t = int(x + t * (x_f_1 - x))
        y_t = int(y + t * (y_f_1 - y))

        if y_t + p_dist > restrictions[2]:
            y_t_p = y_t - p_dist
        else:    
            y_t_p = y_t + p_dist

        trajectory.append([x_t, y_t])
        p_trajectory.append([x_t, y_t_p])
    
    # Second triangle

    y_f_2 = copy.deepcopy(y_f)
    x_f_2 = x_f - (abs(x - x_f) // 2)

    # Discretize the line using linear interpolation
    num_steps = max(abs(x_f_1 - x_f_2), abs(y_f_1 - y_f_2)) // steps

    for i in range(int(num_steps + 1)):
        t = i / num_steps
        x_t = int(x_f_1 + t * (x_f_2 - x_f_1))
        y_t = int(y_f_1 + t * (y_f_2 - y_f_1))

        if p_trajectory[-1][1] < y_t:
            y_t_p = y_t - p_dist
        else:
            y_t_p = y_t + p_dist

        trajectory.append([x_t, y_t])
        p_trajectory.append([x_t, y_t_p])

    # Third triangle

    y_f_3 = y_f - h
    x_f_3 = x_f - (abs(x - x_f) // 4)

    # Discretize the line using linear interpolation
    num_steps = max(abs(x_f_2 - x_f_3), abs(y_f_2 - y_f_3)) // steps

    for i in range(int(num_steps + 1)):
        t = i / num_steps
        x_t = int(x_f_2 + t * (x_f_3 - x_f_2))
        y_t = int(y_f_2 + t * (y_f_3 - y_f_2))

        if p_trajectory[-1][1] < y_t:
            y_t_p = y_t - p_dist
        else:
            y_t_p = y_t + p_dist

        trajectory.append([x_t, y_t])
        p_trajectory.append([x_t, y_t_p])

    # Discretize the line using linear interpolation
    num_steps = max(abs(x_f_3 - x_f), abs(y_f_3 - y_f)) // steps

    for i in range(int(num_steps + 1)):
        t = i / num_steps
        x_t = int(x_f_3 + t * (x_f - x_f_3))
        y_t = int(y_f_3 + t * (y_f - y_f_3))

        if p_trajectory[-1][1] < y_t:
            y_t_p = y_t - p_dist
        else:
            y_t_p = y_t + p_dist
        

        trajectory.append([x_t, y_t])
        p_trajectory.append([x_t, y_t_p])

    

    return trajectory, p_trajectory





    