import numpy as np


class Camera:

    def __init__(self, px, py, pz, lx, ly, lz, ux, uy, uz, d, w):
        self.pos = (float(px), float(py), float(pz))
        self.look_at = (float(lx), float(ly), float(lz))
        self.up = (float(ux), float(uy), float(uz))
        self.distance = d
        self.width = w

        self.dir = self.calc_direction()
        self.fu = self.fix_up()

    def calc_direction(self):
        vec = tuple(np.subtract(self.look_at, self.pos))
        return tuple(vec / np.linalg.norm(vec))

    def fix_up(self):
        right = np.cross(self.dir, self.up)
        right = tuple(right / np.linalg.norm(right))
        vec = np.cross(self.dir, right)     # maybe opposite
        return tuple(vec / np.linalg.norm(vec))

