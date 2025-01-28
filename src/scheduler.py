from functionalities.trajectories import line, circle, square, sawtooth
import numpy as np

class Scheduler:
    def __init__(self):
        self.traj = {
            1: "line",
            2: "circle",
            3: "square",
            4: "sawtooth"
        }

    def scheduler(self):
        traj_opt = np.random.randint(1, 5)
        dir_options = ["horizontal", "vertical"]
        dir_opt = np.random.choice(dir_options)

        x_pos = np.random.randint(20, 180)
        y_pos = np.random.randint(20, 180)

        return self.trajectories(traj_name=self.traj[traj_opt],
                                 direction=dir_opt,
                                 restrictions=(18,18,188,188),
                                 steps=np.random.choice([1,2,3], p=[0.6, 0.3, 0.1]),
                                 player_dim=16,
                                 player_pos=[x_pos,y_pos],
                                 traj_dist=np.random.randint(20, 40),
                                 player_dist=30,
                                 radius=np.random.randint(20, 50),
                                 angle=np.random.randint(20, 60))

    def trajectories(self, traj_name, direction, restrictions, steps, player_dim, player_pos, traj_dist, player_dist, radius, angle):
        if traj_name == "line":
            e_traj, p_traj = line(direction=direction,
                              restrictions=restrictions,
                                steps=steps,
                                 player_dim=player_dim,
                                  player_pos=player_pos,
                                   traj_dist=traj_dist,
                                    player_dist=player_dist)
        elif traj_name == "square":
            e_traj, p_traj = square(restrictions=restrictions,
                                steps=steps,
                                 player_dim=player_dim,
                                  player_pos=player_pos,
                                   p_dist=player_dist)
        elif traj_name == "circle":
            e_traj, p_traj = circle(restrictions=(restrictions[2],restrictions[2]),
                                steps=steps,
                                player_pos=player_pos,
                                radius= radius,
                                p_radius= player_dist)
        elif traj_name == "sawtooth":
            e_traj, p_traj = sawtooth(restrictions=restrictions,
                                angle = angle,
                                steps=steps,
                                player_dim=player_dim,
                                player_pos=player_pos,
                                traj_dist=traj_dist,
                                p_dist=player_dist)
        return e_traj, p_traj
        
        """
        line(direction=direction,
                              restrictions=(18,18,188,188),
                                steps=1,
                                 player_dim=16,
                                  player_pos=[160,25],
                                   traj_dist=40,
                                    player_dist=30)

        square(restrictions=(18,18,188,188),
                                steps=1,
                                 player_dim=16,
                                  player_pos=[160,25],
                                   p_dist=28)

        circle(restrictions=(188,188),
                                steps=1,
                                player_pos=[160,25],
                                radius= 50,
                                p_radius= 20)

        e_traj, p_traj = sawtooth(restrictions=(18,18,188,188),
                                angle = 60,
                                steps=1,
                                player_dim=16,
                                player_pos=[50,100],
                                traj_dist=40,
                                p_dist=28)
        """