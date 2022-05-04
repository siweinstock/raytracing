class Light:

    def __init__(self, px, py, pz, r, g, b, spec, shadow, width):
        self.pos = (px, py, pz)
        self.color = (r, g, b)
        self.specular = spec
        self.shadow = shadow
        self.width = width

