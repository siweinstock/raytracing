import utils
import sys
from Screen import Screen
from Intersection import find_intersection
# from Parser import parse
# import Tracer
from Scene import Scene
import numpy as np

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


setup = {'spheres': [], 'boxes': [], 'materials': [], 'planes': [], 'lights': []}


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def parse_args(args):
    dim = [int(args[2]) if len(args) > 2 else 500, int(args[3]) if len(args) > 3 else 500]
    return args[0], args[1], (tuple(dim))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    f_in, f_out, dim = parse_args(sys.argv[1:])
    print(dim)

    camera, scene = utils.parse_scene(r'pool.txt', setup)
    scrn = Screen(camera, dim)

    # print(setup['spheres'][-1].ctr, setup['spheres'][-1].R, setup['spheres'][-1].idx)
    # find_intersection(scene, None)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
