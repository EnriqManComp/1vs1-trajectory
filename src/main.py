import os
from environment.environment import Simulator
from environment.world import Simple
from cfg import cfg
import gc
from functionalities.trajectories import line, circle, square, sawtooth


#os.environ["SDL_VIDEODRIVER"] = "dummy"

sim = Simulator()

load = False
train = False
collect_data_from_traj = True


best_score = 0.0

if train:
    MAX_EPISODES = cfg.EPISODES
elif collect_data_from_traj:
    MAX_EPISODES = cfg.COLLECT_DATA
else:
    MAX_EPISODES = cfg.TEST

for episode in range(1, MAX_EPISODES):

    if collect_data_from_traj:
        
        # Create environment
        train_env = Simple()
        
        # Create trajectories
        #e_traj, p_traj = circle((200,200), (18,18,188,188), 1, 16, [160,25], 50, 20)
        """
        e_traj, p_traj = line(direction="horizontal",
                              restrictions=(18,18,188,188),
                                steps=1,
                                 player_dim=16,
                                  player_pos=[160,25],
                                   traj_dist=40,
                                    player_dist=30)
        """
        """
        e_traj, p_traj = square(restrictions=(18,18,188,188),
                                steps=1,
                                 player_dim=16,
                                  player_pos=[160,25],
                                   p_dist=28)
        """
        """
        e_traj, p_traj = circle(restrictions=(188,188),
                                steps=1,
                                player_pos=[160,25],
                                radius= 50,
                                p_radius= 20)
        """

        e_traj, p_traj = sawtooth(restrictions=(18,18,188,188),
                                steps=1,
                                player_dim=16,
                                player_pos=[160,25],
                                p_dist=28)
                                
        # Collect data from trajectories
        sim.collect_data_from_traj(env=train_env,
                                   trajectory= e_traj,
                                    p_trajectory= p_traj,
                                   p_pos = [160,50],
                                   e_pos = [160,25],
                                   time=cfg.TIME,
                                   backward_option=True,
                                   plot_lasers=False,
                                   cycles=2)
        train_env.end_env()

        gc.collect()
