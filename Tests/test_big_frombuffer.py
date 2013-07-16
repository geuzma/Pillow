import sys
import os

if "--installed" in sys.argv:
    sys_path_0 = sys.path[0]
    del sys.path[0]

from PIL import Image

if "--installed" in sys.argv:
    sys.path.insert(0, sys_path_0)
ROOT = '.'


print("-"*68)
print("Python modules loaded from", os.path.dirname(Image.__file__))
print("Binary modules loaded from", os.path.dirname(Image.core.__file__))
print("-"*68)

#im = Image.open(os.path.join(ROOT, "Images/lena.jpg"))
#im.load()
#size = int(sys.argv[2]) 
size = 15000
byte_size  = size * size  * 3 * 4
print "byte_size: ", byte_size
print "int_max:   ", 2**32 / 2
print "byte_size > int_max: ", byte_size > 2**32 / 2


#im = Image.new("RGB", (size, size))
#print im

import numpy as np
buff = np.random.randint(0, 256, (size, size, 3))

im = Image.frombuffer('RGB', (size, size), buff, 'raw', 'RGB', 0, 1)
if im == None:
    print "frombuffer failed"
else:
    print im
