from functionalities.trajectories import line, circle, square, sawtooth

class Scheduler:
    def __init__(self):
        self.traj = {
            "line": line,
            "circle": circle,
            "square": square,
            "sawtooth": sawtooth
        }

    def scheduler(self):

        pass

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