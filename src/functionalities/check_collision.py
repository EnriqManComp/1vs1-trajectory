
class CheckCollision:

    def check_collisions(self, main_rect, target_rect, obstacles_rect):
        
        if main_rect.colliderect(obstacles_rect[2]):                        
            #print("COLISION#####################################################################################################################")
            return True
        # Check upper wall collision
        elif main_rect.colliderect(obstacles_rect[0]):            
            
            #print("COLISION#####################################################################################################################")
            return True
        # Check right wall collision
        elif main_rect.colliderect(obstacles_rect[3]):
            
            #print("COLISION#####################################################################################################################")
            return True
        # Check bottom wall collision
        elif main_rect.colliderect(obstacles_rect[1]):
            
            #print("COLISION#####################################################################################################################")
            return True
        # Check collision with the evasor
        elif main_rect.colliderect(target_rect):
            #print("COLISION#####################################################################################################################")
            return True
        
        else:
            return False