class Setting:

    def __init__(self, bgr, bgg, bgb, sh_rays, rec_max, ss):
        self.bg = (bgr, bgg, bgb)
        self.shadow_rays = sh_rays
        self.recursion = rec_max
        self.ss = ss
