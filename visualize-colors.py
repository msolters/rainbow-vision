#!/usr/bin/env python3
"""
RGB Image Analysis with Python

usage:
    me.py <image_in> 
    me.py <image_in> <image_analysis_out>
"""
import sys

#import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

__version__ = "0.2.0"

try:
    xrange # Python2
except:
    xrange = range # Python3

# (1) Import the file to be analyzed!
if len(sys.argv) < 2:
    img_file = Image.open("thedress.jpg")
else:
    img_file = Image.open(sys.argv[1])

img = img_file.load()

# (2) Construct a blank matrix representing the pixels in the image
[xs, ys] = img_file.size
max_intensity = 100
hues = {}

# (3) Examine each pixel in the image file
for x in xrange(0, xs):
  for y in xrange(0, ys):
    # ( )  Get the RGB color of the pixel
    [r, g, b] = img[x, y]

    # ( )  Normalize pixel color values
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # ( )  Convert RGB color to HSV
    [h, s, v] = colorsys.rgb_to_hsv(r, g, b)
    if h not in hues:
      hues[h] = {}
    if v not in hues[h]:
      hues[h][v] = 1
    else:
      if hues[h][v] < max_intensity:
        hues[h][v] += 1

# ( )   Decompose the hues tree into a set of dimensional arrays we can use with matplotlib
h_ = []
v_ = []
i = []
colours = []

for h in hues:
  for v in hues[h]:
    h_.append(h)
    v_.append(v)
    i.append(hues[h][v])
    [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
    colours.append([r, g, b])

# ( )   Plot the graph!
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.scatter(h_, v_, i, s=5, c=colours, lw=0)

ax.set_xlabel('Hue')
ax.set_ylabel('Value')
ax.set_zlabel('Intensity')
fig.add_axes(ax)
if len(sys.argv) < 3:
    plt.show()
else:
    plt.savefig(sys.argv[2])

