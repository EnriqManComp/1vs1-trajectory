import matplotlib.pyplot as plt
# 

def viz(plane):
    
    matrix_255 = plane * 255

    # Visualize with Matplotlib
    plt.imshow(matrix_255)
    plt.colorbar(label='Pixel Intensity')
    plt.title('Boolean Matrix Visualization')
    plt.show()
