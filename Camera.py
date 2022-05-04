import numpy as np
import utils


class Camera:

    def __init__(self, px, py, pz, lx, ly, lz, ux, uy, uz, d, w):
        self.pos = (float(px), float(py), float(pz))
        self.look_at = (float(lx), float(ly), float(lz))
        # self.up = (float(ux), float(uy), float(uz))
        self.up = utils.normalize((float(ux), float(uy), float(uz)))     # normalized
        self.distance = float(d)
        self.width = float(w)

        self.towards = utils.normalize(np.subtract(self.look_at, self.pos))     # normalized

        # self.towards = self.calc_direction()    # normalized
        # self.fu = self.fix_up()

    # def calc_direction(self):
    #     vec = tuple(np.subtract(self.look_at, self.pos))
    #     return tuple(vec / np.linalg.norm(vec))

    # def fix_up(self):
    #     right = np.cross(self.towards, self.up)
    #     right = tuple(right / np.linalg.norm(right))
    #     vec = np.cross(self.towards, right)     # maybe opposite
    #     return tuple(vec / np.linalg.norm(vec))

