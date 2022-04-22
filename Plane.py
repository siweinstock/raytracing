class Plane:

    def __init__(self, nx, ny, nz, offset, idx):
        self.normal = (float(nx), float(ny), float(nz))
        self.offset = offset
        self.idx = idx
