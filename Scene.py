class Scene:

    def __init__(self, setting, materials, spheres, planes, boxes, lights):
        self.setting = setting
        self.materials = materials
        self.spheres = spheres
        self.planes = planes
        self.boxes = boxes
        self.lights = lights
        self.primitives = spheres + planes + boxes
