# Imports
from __future__ import division
import numpy as np
import os
import glob
from PIL import Image
from random import *
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def writer_map():
    d = {}
    with open('forms.txt') as f:
        for line in f:
            if line[0] == '#':
                continue
            key = line.split(' ')[0]
            writer = line.split(' ')[1]
            d[key] = writer
    return d


def parse_file(d):
    tmp = []
    target_list = []
    for root, directories, filenames in os.walk('dataset'):
        for filename in filenames:
            img_path = os.path.join(root, filename)
            tmp.append(img_path)
            file, ext = os.path.splitext(filename)
            parts = file.split('-')
            form = parts[0] + '-' + parts[1]
            for key in d:
                if key == form:
                    target_list.append(str(d[form]))

    img_files = np.asarray(tmp)
    img_targets = np.asarray(target_list)
    return img_files, img_targets



d = writer_map()
img_files, img_targets = parse_file(d)

# # Test Code
# print(img_targets[:10])
# print(img_files[:10])
# print(len(img_files))
# print(len(img_targets))

# Show the images

for filename in img_files[:3]:
    img=mpimg.imread(filename)
    plt.figure(figsize=(10,10))
    plt.imshow(img, cmap ='gray')
    plt.show()

