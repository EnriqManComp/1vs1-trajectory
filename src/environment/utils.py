from PIL import Image
import numpy as np
import os

class PlaneSaver:
    def __init__(self, root_dir, episode_number):
        self.database_counter = 0
        self.root_dir = root_dir
        self.episode_number = episode_number

    def set_episode_number(self, episode_number):
        self.episode_number = episode_number

    # Function to save binary plane as an image
    def save_plane_as_image(self, plane, filename):
        plane = (plane * 255).astype(np.uint8)  # Convert to uint8 (0 → black, 255 → white)
        img = Image.fromarray(plane, mode="L")  # "L" mode for grayscale
        
        # Construct the directory path
        dir_path = os.path.join(self.root_dir, str(self.episode_number), str(self.database_counter))
        
        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)
        # Construct the file path
        file_path = os.path.join(dir_path, filename)

        # Save the image
        img.save(file_path)

    def save_planes_img(self, first_plane, second_plane, third_plane, fourth_plane, sixth_to_fourteen_plane, reward_plane, distance_plane, twenty_first_plane):
        """
        Save the planes as images
        """
        self.save_plane_as_image(first_plane, 'first_plane.png')
        self.save_plane_as_image(second_plane, 'second_plane.png')
        self.save_plane_as_image(third_plane, 'third_plane.png')
        self.save_plane_as_image(fourth_plane, 'fourth_plane.png')

        #save_matrix_as_image(sixth_to_fourteen_plane, 'sixth_to_fourteen_plane.png')
        self.save_plane_as_image(reward_plane, 'reward_plane.png')
        self.save_plane_as_image(distance_plane, 'distance_plane.png')
        self.save_plane_as_image(twenty_first_plane, 'twenty_first_plane.png')

        self.database_counter += 1


        