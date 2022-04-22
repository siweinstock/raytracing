from Parser import parse
import numpy as np

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scene = parse(r'pool.txt')
    print(np.linalg.norm(scene.camera.dir))
    print(scene.camera.dir)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
