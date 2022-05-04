from math import sqrt

import numpy as np

import Camera


class Screen:

    def __init__(self, cam: Camera):
        self.height = 500
        self.width = 500

        self.Sx = -cam.dir[1]
        self.Cx = sqrt(1-self.Sx**2)
        self.Sy = - (cam.dir[0] // self.Cx)
        self.Cy = cam.dir[2] // self.Cx

        self.Vx = (self.Cy, 0.0, self.Sy)
        self.Vy = (-self.Sy*self.Sx, self.Cx, self.Cy*self.Sx)
        self.Vz = (-self.Sy*self.Cx, -self.Sx, self.Cy*self.Cx)

        self.P0 = self.get_p0(cam)

    # formula from page 16
    def get_p0(self, cam: Camera):
        p = np.add(cam.pos, cam.distance * self.Vz)
        # p0 = p - w*Vx - h*Vy
        return np.subtract(np.subtract(p, 0.5*self.height*np.array(self.Vy)), 0.5*self.height*np.array(self.Vx))
