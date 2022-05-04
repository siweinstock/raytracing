from itertools import count


class Material:
    _idx = count(1)

    def __init__(self, dr, dg, db, sr, sg, sb, rr, rg, rb, phong, trans):
        self.diffuse = (float(dr), float(dg), float(db))
        self.specular = (float(sr), float(sg), float(sb))
        self.reflection = (float(rr), float(rg), float(rb))
        self.phong = float(phong)
        self.transparency = float(trans)
        self.index = next(self._idx)


