from .check_collision import CheckCollision

class CheckFutureMovement:
    def __init__(self):
        self.check_collision = CheckCollision()

    def check(self, current_player, pursuiter_rect, evasor_rect, obstacles_rect):
        if current_player == "pursuiter":
            return self.check_collision.check_collisions(main_rect=pursuiter_rect,
                                                         target_rect=evasor_rect, 
                                                         obstacles_rect=obstacles_rect)
        else:
            return self.check_collision.check_collisions(main_rect=evasor_rect,
                                                         target_rect=pursuiter_rect,
                                                          obstacles_rect=obstacles_rect)
        
       