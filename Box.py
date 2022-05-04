from Plane import Plane


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
