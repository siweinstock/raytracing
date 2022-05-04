import numpy as np
from Camera import Camera
from Scene import Scene
import Screen
from Ray import Ray
from Intersection import Intersection


def cast(cam: Camera, scn: Scene, dim: tuple, scrn: Screen):
    h, w = dim
    # image = np.ndarray(shape=dim, )

    # set P0
    p0 = scrn.get_p0(cam)

    # shoot a ray through each pixel in the image
    for i in range(h):
        p = p0

        for j in range(w):
            ray = Ray(cam.pos, p)
            # hit = find_intersection()
            # image[i, j] = get_color()

            p = np.add(p, (scrn.Vx, 0, 0))

        p0 = np.add(p0, (0, scrn.Vy, 0))


class Tracer:

    def __init__(self):
        pass

    # main loop from page 16






