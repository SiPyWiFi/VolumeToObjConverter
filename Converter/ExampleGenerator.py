import numpy as np

def return_example_volume():
    width, height, depth = 101, 121, 89
    dimensions = (width, height, depth)

    array = np.ones(dimensions)*10
    array[:width//2, :, :] = 5
    array[width//10:-width//10, height//10:-height//10, depth//10:-depth//10] = 15

    return array



