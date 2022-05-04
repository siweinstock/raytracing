import numpy as np


class Ray:

    def __init__(self, start, end):
        self.P0 = start                                                                 # ray's starting point
        self.V = np.subtract(end, start) // np.linalg.norm(np.subtract(end, start))     # ray's direction
