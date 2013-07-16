# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

import sys

if "--installed" in sys.argv:
    sys_path_0 = sys.path[0]
    del sys.path[0]

from PIL import Image

if "--installed" in sys.argv:
    sys.path.insert(0, sys_path_0)

im = Image.open('d:/data/vms/big4.jpg')

print "size / 2GB:", im.size[0] * im.size[1] * 3 / float(2**31)
c = im.crop([1000, 1000, 2000, 2000])

print c
#imshow(c)

