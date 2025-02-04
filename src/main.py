import os
from environment.environment import Simulator
from environment.world import Simple
from cfg import cfg
import gc
from scheduler import Scheduler



#os.environ["SDL_VIDEODRIVER"] = "dummy"

sim = Simulator()
scheduler = Scheduler()

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
        e_traj, p_traj = scheduler.scheduler()
        
        """
        e_traj, p_traj = scheduler.trajectories(
            traj_name="sawtooth",
            direction="vertical",
            restrictions=(18,18,188,188),
            steps=1,
            player_dim=8,
            player_pos=[160,25],
            traj_dist=40,
            player_dist=30,
            radius=50,
            angle=60
        )
        """
        
        # Collect data from trajectories
        sim.collect_data_from_traj(
                                    episode=episode,
                                    env=train_env,
                                   trajectory= e_traj,
                                    p_trajectory= p_traj,
                                   p_pos = [160,50],
                                   e_pos = [160,25],
                                   time=cfg.TIME,
                                   backward_option=False,
                                   plot_lasers=False,
                                   cycles=2)
        
        train_env.end_env()

        gc.collect()
