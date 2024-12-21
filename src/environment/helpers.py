import pygame
import numpy as np

r = 5
danger_zone = 25
taget_zone = 40

def plot_area(surface, color, pos, r):

    """
    Plot target area around a position

    """
    
    pygame.draw.circle(surface, color, (pos[0], pos[1]), r)

def get_laser_measurements(evasor_pos, lasers, obstacles):
        
        I = []

        for l, laser in enumerate(lasers):
            #print("Laser: ", l, laser[2])
            check_evasor = False
            # Get laser general equation
            L1 = line(laser[0], laser[1])

            evasor_intercept, evasor_angle = get_evasor_intersection(evasor_pos, laser)              
            #print("Evasor intercept: ", evasor_intercept)
            if evasor_intercept != False:   
                           
                if check_laser_evasor_angle(evasor_angle, laser[2]):           
                    check_evasor = True
                    I.append(np.sqrt((laser[0][0] - evasor_intercept[0])**2 + (laser[0][1] + evasor_intercept[1])**2))
                    continue           

            for obst in obstacles:                
                
                # Get obstacle general equation
                L2 = line(obst[0], obst[1])

                # Get interception between the laser and the obstacle
                
                intercept = intersection(L1, L2)
                
                if intercept != None and check_evasor == False:                    
                    if check_laser_angle(laser[2], obst[2]):      
                        #print(intercept)                 
                        I.append(np.sqrt((laser[0][0] - intercept[0])**2 + (laser[0][1] - intercept[1])**2))
                        break                   
        # Standarize
        I = np.array(I)
        #I = (I - I.mean()) / I.std()
        return I

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[1]*p2[0] - p2[1]*p1[0])
    return A, B, C

def get_evasor_intersection(evasor_pos, laser):
    #print("Laser angle: ", laser[2])
    y1 = -laser[0][1]
    y2 = -laser[1][1]
    x1 = laser[0][0]
    x2 = laser[1][0]
    #print("X1: ", x1, " Y1: ", y1, " X2: ", x2, " Y2: ", y2)
    c_center = (evasor_pos[0], evasor_pos[1])
    
    # Get slope
    if x2 - x1 == 0:
        x2 = x2 + 0.0001
    m = round(((y2 - y1) / (x2 - x1)), 2)
    # Get y intercept
    b = round((y1 - m * x1),2)

    

    A = round(1 + m**2, 2)
    B = round(-2*(c_center[0] + m*(-b + c_center[1])),2)
    C = round(c_center[0]**2 + (c_center[1]-b)**2 - r**2, 2)
    
    D = round((B**2 - 4*A*C), 2)
    
    
    if D > 0:
        x1_ = round((-B + np.sqrt(D)) / (2*A), 2)
        x2_ = round((-B - np.sqrt(D)) / (2*A), 2)

        y1_ = round(m*x1_ + b, 2)
        y2_ = round(m*x2_ + b, 2)
        
        if x1_ < evasor_pos[0]-r*2 or x1_ > evasor_pos[0]+r*2:
            return False, False
        elif x2_ < evasor_pos[0]-r*2 or x2_ > evasor_pos[0]+r*2:
            return False, False
        elif y1_ < evasor_pos[1]-r*2 or y1_ > evasor_pos[1]+r*2:
            return False, False
        elif y2_ < evasor_pos[1]-r*2 or y2_ > evasor_pos[1]+r*2:
            return False, False
        evasor_angle = get_angle(evasor_pos[0], evasor_pos[1], laser[0][0], laser[0][1])
        return (x1_, y1_), evasor_angle
    else:
        
        return False, False

def check_laser_evasor_angle(evasor_angle, laser_angle):
    # Laser angle and evasor angle go oposite
    laser_angle = 360 - laser_angle

    #print("Evasor angle: ", evasor_angle, " Laser angle: ", laser_angle)
    if (evasor_angle >= 0 and evasor_angle <= 90) and (laser_angle >= 0 and laser_angle <= 90):
        return True
    elif (evasor_angle >= 90 and evasor_angle <= 180) and (laser_angle >= 90 and laser_angle <= 180):
        return True
    elif (evasor_angle >= 180 and evasor_angle <= 270) and (laser_angle >= 180 and laser_angle <= 270):
        return True
    elif (evasor_angle >= 270 and evasor_angle <= 360) and (laser_angle >= 270 and laser_angle <= 360):
        return True       
    else:
        return False
    
def intersection(L1, L2):

    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    
    if D != 0:
        x = Dx / D
        

        # Aqui se quita la posibilidad de que se seleccione una interseccion fuera de los limites del entorno
        # Por lo tanto, se descarta tambien cuando antes esta el limite izquierdo y se detecta primero el limite inferior
        if x > 200.0 or x < 0.0:
            return None
        
        y = Dy / D
        #print("Discriminant", D, "x: ", x, " y: ", y)
        if y >-0.0 or y<-200.0:
            return None
        
        return x,y
    else:
        return None
    
def check_laser_angle(laser_angle, obst_name):
        
    if obst_name == "up":
        if (laser_angle == 270) or (laser_angle > 180 and laser_angle < 270) or (laser_angle > 270 and laser_angle < 360):
            return True
        else:
            return False
    
    elif obst_name == "down":
        if (laser_angle == 90) or (laser_angle > 0 and laser_angle < 90) or (laser_angle > 90 and laser_angle < 180):
            return True
        else:
            return False
        
    elif obst_name == "left":
        if (laser_angle == 180) or (laser_angle > 90 and laser_angle < 180) or (laser_angle > 180 and laser_angle < 270):
            return True
        else:
            return False
        
    elif obst_name == "right":
        if (laser_angle == 0) or (laser_angle == 360) or (laser_angle > 0 and laser_angle < 90) or (laser_angle > 270 and laser_angle < 360):
            return True
        else:
            return False
        
def get_angle(x1, y1, x2, y2):
    if (x2 - x1) == 0 and (y2 > y1):
        return 270
    elif (x2 - x1) == 0 and (y2 < y1):
        return 90
    angle = np.arctan((y2 - (-y1)) / (x2 - x1))
    angle = np.degrees(angle) 

    if abs(angle) == 0.0 and x1 < x2:
        angle = 180
    elif abs(angle) == 0.0 and x1 > x2:
        angle = 0
    elif angle < 0 and x1 < x2:
        angle = 180 + angle
    elif angle > 0 and x1 < x2:
        angle = 180 + angle
    elif angle < 0 and x1 > x2:
        angle = 360 + angle 

    return angle 