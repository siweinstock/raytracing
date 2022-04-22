from Sphere import Sphere
from Camera import Camera
from Material import Material
from Setting import Setting
from Plane import Plane
from Light import Light
from Box import Box
from Scene import Scene

spheres = []
boxes = []
cubes = []
materials = []
planes = []
lights = []


def parse(file):
    with open(file) as f:
        for line in f:
            if line[0] == '#' or len(line) == 1:
                continue

            arr = list(filter(None, line.strip('\n').replace(' ', '\t').split('\t')))

            if arr[0] == "sph":
                spheres.append(Sphere(*arr[1:]))
                # print("Sphere: ", end=' ')
                # print(spheres[-1].pos, spheres[-1].radius, spheres[-1].idx)
            elif arr[0] == "cam":
                camera = Camera(*arr[1:])
                # print("Camera: ", end=' ')
                # print(camera.pos, camera.look_at)
            elif arr[0] == "mtl":
                materials.append(Material(*arr[1:]))
                # print("Material: ", end=' ')
                # print(materials[-1].diffuse, materials[-1].specular)
            elif arr[0] == "set":
                setting = Setting(*arr[1:])
                # print("Setting: ", end=' ')
                # print(setting.bg, setting.ss)
            elif arr[0] == "pln":
                planes.append(Plane(*arr[1:]))
                # print("Plane: ", end=' ')
                # print(planes[-1].normal, planes[-1].offset, planes[-1].idx)
            elif arr[0] == "box":
                boxes.append(Box(*arr[1:]))
                # print("Box: ", end=' ')
                # print(boxes[-1].pos, boxes[-1].length, boxes[-1].idx)
            elif arr[0] == "lgt":
                lights.append(Light(*arr[1:]))
                # print("Light: ", end=' ')
                # print(lights[-1].pos, lights[-1].color, lights[-1].specular)
            else:
                print("Error!")

    # return scene
    return Scene(camera, setting, materials, spheres, planes, boxes, lights)




