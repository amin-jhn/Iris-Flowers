# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum(np.square(new_points.reshape(new_points.shape[0], 1, new_points.shape[1]) - points), axis=2)
