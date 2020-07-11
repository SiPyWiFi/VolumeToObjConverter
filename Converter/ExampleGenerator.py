import numpy as np

def return_example_volume():
    # 3d volume to test
    width, height, depth = 101, 121, 89
    dimensions = (width, height, depth)

    array = np.ones(dimensions)*10
    array[10:20, 10:30, 10:20] = np.ones((10, 20, 10)) * 20

    return array



