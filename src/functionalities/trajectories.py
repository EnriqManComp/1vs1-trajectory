import numpy as np
import copy
import matplotlib.pyplot as plt

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
        p_trajectory[i][1] += player_dist

    return trajectory, p_trajectory

def circle(world_dim, restrictions, steps, player_dim, player_pos, radius, p_radius):
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

    # Initial position
    x, y = player_pos

    # Circle parameters
    center = [world_dim[0] // 2, world_dim[1] // 2]

    # Discretize the circle using parametric equations
    for i in range(0, 360, steps):
        angle = np.radians(i)
        x_t = int(center[0] + radius * np.cos(angle))
        y_t = int(center[1] + radius * np.sin(angle))
        trajectory.append([x_t, y_t])

    for i in range(0, 360, steps):
        angle = np.radians(i)
        x_t = int(center[0] + p_radius * np.cos(angle))
        y_t = int(center[1] + p_radius * np.sin(angle))
        p_trajectory.append([x_t, y_t])

    

    return trajectory, p_trajectory

def sinusoidal_trajectory(world_dim, restrictions, steps, player_dim, player_pos, amplitude):
    """
    Generate a sinusoidal trajectory for the player.

    Args:
        world_dim: tuple, (width, height)
        restrictions: tuple, (start, end) range for x-axis.
        steps: int, number of steps that the player will take.
        player_dim: int, player dimension.
        player_pos: list, player position [x, y].
        amplitude: float, amplitude of the sinusoidal wave.

    Returns:
        trajectory: list, list of positions for the player.
    """
    # Validate inputs
    if steps <= 0 or amplitude <= 0:
        raise ValueError("Steps and amplitude must be positive.")

    start = player_pos[0]
    end = copy.deepcopy(start)
    while True:
        if (abs(end - start) < 40) or (end < restrictions[0] + player_dim) or (end > restrictions[2] - player_dim):
            end = np.random.randint(start, restrictions[2] - player_dim)
        else:
            break

    x_positions = np.linspace(start, end, steps) # Discretize x-axis values

    y_positions = amplitude * np.sin(x_positions)  # Calculate y values based on sine wave

    # Round y values to integers
    y_positions = np.round(y_positions)
    # Round x values to integers
    x_positions = np.round(x_positions)

    trajectory = []
    for x, y in zip(x_positions, y_positions):
        trajectory.append([int(x), int(player_pos[1] + y)])  # Adjust y relative to player position

    

    return trajectory




    