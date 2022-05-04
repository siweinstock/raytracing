import numpy as np
from Ray import Ray
import utils


EPSILON = 0.001


class Sphere:

    def __init__(self, cx, cy, cz, radius, idx):
        self.ctr = (float(cx), float(cy), float(cz))
        self.R = float(radius)
        self.idx = int(idx)

    def intersect(self, p: tuple, ray: Ray):
        L = np.subtracy(self.ctr, ray.P0)  # L = O-P0
        tca = np.dot(L, ray.V)

        if tca < 0:
            return 0

        dsq = np.dot(L, L) - tca ** 2  # d^2=L*L-tca^2
        rsq = self.R ** 2

        if dsq > rsq:
            return 0

        thc = np.sqrt(rsq - dsq)
        return tca - thc

    def get_normal(self, p0):
        return utils.normalize(np.subtract(p0, self.ctr))


class Plane:

    def __init__(self, nx, ny, nz, offset, idx):
        self.N = (float(nx), float(ny), float(nz))
        self.offset = offset
        self.idx = idx

    # based on page 9
    def intersect(self, ray: Ray):
        prod = np.dot(self.N, ray.V)
        if abs(prod) < EPSILON:     # parallel or unified
            return 1 if self.offset == 0 else None
        else:
            p0 = self.offset * self.N
            t = np.dot(np.subtract(p0, ray.P0), self.N) / prod
            return None if t < 0 else 2


class Box:

    def __init__(self, px, py, pz, length, idx):
        self.ctr = (px, py, pz)
        self.length = length
        self.idx = idx

    # create a plane for each face of the box (the box is parallel to axis)
    def get_faces(self):
        return [Plane(1, 0, 0, self.ctr[0] + 0.5 * self.length, self.idx),
                Plane(1, 0, 0, self.ctr[0] - 0.5 * self.length, self.idx),
                Plane(0, 1, 0, self.ctr[1] + 0.5 * self.length, self.idx),
                Plane(0, 1, 0, self.ctr[1] - 0.5 * self.length, self.idx),
                Plane(0, 0, 1, self.ctr[2] + 0.5 * self.length, self.idx),
                Plane(0, 0, 1, self.ctr[2] - 0.5 * self.length, self.idx)]
