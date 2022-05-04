import numpy as np
from Scene import Scene, Setting
from Primitives import Sphere, Plane, Box
from Camera import Camera
from Material import Material
# from Setting import Setting
from Light import Light


# Normalize a vector
def normalize(vector: tuple):
    return tuple(vector / np.linalg.norm(vector))


# Export scene to an image file
def export_image(path, scn: Scene):
    pass


def parse_scene(file, setup: dict):

    with open(file) as f:
        for line in f:
            if line[0] == '#' or len(line) == 1:
                continue

            arr = list(filter(None, line.strip('\n').replace(' ', '\t').split('\t')))

            if arr[0] == "sph":
                setup['spheres'].append(Sphere(*arr[1:]))
                print("Sphere: ", end=' ')
                print(setup['spheres'][-1].ctr, setup['spheres'][-1].R, setup['spheres'][-1].idx)
            elif arr[0] == "cam":
                camera = Camera(*arr[1:])
                print("Camera: ", end=' ')
                print(camera.pos, camera.look_at)
            elif arr[0] == "mtl":
                setup['materials'].append(Material(*arr[1:]))
                print("Material: ", end=' ')
                print(setup['materials'][-1].index, setup['materials'][-1].diffuse, setup['materials'][-1].specular)
            elif arr[0] == "set":
                setting = Setting(*arr[1:])
                print("Setting: ", end=' ')
                print(setting.bg, setting.ss)
            elif arr[0] == "pln":
                setup['planes'].append(Plane(*arr[1:]))
                print("Plane: ", end=' ')
                print(setup['planes'][-1].N, setup['planes'][-1].offset, setup['planes'][-1].idx)
            elif arr[0] == "box":
                setup['boxes'].append(Box(*arr[1:]))
                print("Box: ", end=' ')
                print(setup['boxes'][-1].pos, setup['boxes'][-1].length, setup['boxes'][-1].idx)
            elif arr[0] == "lgt":
                setup['lights'].append(Light(*arr[1:]))
                print("Light: ", end=' ')
                print(setup['lights'][-1].pos, setup['lights'][-1].color, setup['lights'][-1].specular)
            else:
                print("Error!")

    # return scene
    # return camera, Scene(setting, setup['materials'], setup['spheres'], setup['planes'], setup['boxes'], setup['lights'])
    return camera, Scene(setting, setup)

