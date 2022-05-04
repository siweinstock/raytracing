class Material:
    def __init__(self, dr, dg, db, sr, sg, sb, rr, rg, rb, phong, trans):
        self.diffuse = (dr, dg, db)
        self.specular = (sr, sg, sb)
        self.reflection = (rr, rg, rb)
        self.phong = phong
        self.transparency = trans


