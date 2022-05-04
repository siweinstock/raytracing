class Setting:

    def __init__(self, bgr, bgg, bgb, sh_rays, rec_max, ss):
        self.bg = (bgr, bgg, bgb)
        self.shadow_rays = sh_rays
        self.recursion = rec_max
        self.ss = ss


class Scene:

    def __init__(self, setting, setup):
        self.setting = setting
        self.materials = setup['materials']
        self.spheres = setup['spheres']
        self.planes = setup['planes']
        self.boxes = setup['boxes']
        self.lights = setup['lights']
        self.primitives = self.spheres + self.planes + self.boxes
