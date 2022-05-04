from math import sqrt
import numpy as np
import Camera


class Screen:

    def __init__(self, cam: Camera, dim: tuple):
        self.height, self.width = dim
        self.distance = cam.distance
        self.pixel_size = cam.width / self.width

        self.Sx = -cam.towards[1]
        self.Cx = sqrt(1-self.Sx**2)
        self.Sy = - (cam.towards[0] // self.Cx)
        self.Cy = cam.towards[2] // self.Cx

        self.Vx = (self.Cy, 0.0, self.Sy)
        self.Vy = (-self.Sy*self.Sx, self.Cx, self.Cy*self.Sx)
        self.Vz = (-self.Sy*self.Cx, -self.Sx, self.Cy*self.Cx)

        self.P0 = self.get_p0(cam)

    # formula from page 16
    def get_p0(self, cam: Camera):
        p = np.add(cam.pos, cam.distance * np.array(self.Vz))
        # p0 = p - w*Vx - h*Vy
        return np.subtract(np.subtract(p, 0.5*self.height*np.array(self.Vy)), 0.5*self.height*np.array(self.Vx))
