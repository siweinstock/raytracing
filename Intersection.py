from Scene import Scene
from Ray import Ray
from Plane import Plane
from Sphere import Sphere
from Box import Box
import numpy as np


class Intersection:

    def __init__(self, primitive, t):
        self.primitive = primitive
        self.t = t


epsilon = 0.001


# ray-plane intersection from page 9
def intersect_plane(ray: Ray, plane: Plane):
    return -((np.dot(ray.P0, plane.N) + plane.offset) // np.dot(ray.V, plane.N))


# ray-sphere intersection from page 7
def intersect_sphere(ray: Ray, sphere: Sphere):
    L = np.subtract(sphere.ctr, ray.P0)     # L = O-P0
    tca = np.dot(L, ray.V)

    if tca < 0:
        return 0

    dsq = np.dot(L, L) - tca ** 2     # d^2=L*L-tca^2
    rsq = sphere.R ** 2

    if dsq > rsq:
        return 0

    thc = np.sqrt(rsq - dsq)
    return tca - thc


# TODO using the slabs method
def intersect_box(ray: Ray, box: Box):
    faces = box.get_faces()
    t = []

    for face in faces:
        # plane is parallel to ray
        if np.dot(face.N, ray.V) < epsilon:
            continue

        t.append(intersect_plane(ray, face))

    txmin, txmax = min(t[:2]), max(t[:2])
    tymin, tymax = min(t[2:4]), max(t[2:4])
    tzmin, tzmax = min(t[4:]), max(t[4:])

    if txmin > tymax or tymin > txmax:
        return 0

    if max(txmin, tymin) > tzmin or tzmin > min(txmax, tymax):
        return 0

    return max(txmin, tymin, tzmin)


# find the nearest intersecting primitive as shown in page 11
def find_intersection(scn: Scene, ray: Ray):
    min_t = float("inf")
    min_primitive = None

    for primitive in scn.primitives:
        if isinstance(primitive, Plane):
            # print(str(type(primitive)) + "is plane")
            t = intersect_plane(ray, primitive)
        elif isinstance(primitive, Sphere):
            t = intersect_sphere(ray, primitive)
            # print(str(type(primitive)) + "is sphere")
        elif isinstance(primitive, Box):
            t = intersect_box(ray, primitive)
            # print(str(type(primitive)) + "is box")
        # shouldn't get here
        else:
            t = float("inf")

        if t < min_t:
            min_t = t
            min_primitive = primitive

        return Intersection(min_primitive, min_t)
