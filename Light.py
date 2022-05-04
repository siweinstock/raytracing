class Light:

    def __init__(self, px, py, pz, r, g, b, spec, shadow, width):
        self.pos = (float(px), float(py), float(pz))
        self.color = (float(r), float(g), float(b))
        self.specular = float(spec)
        self.shadow = float(shadow)
        self.width = float(width)   # aka radius

