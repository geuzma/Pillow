from tester import *

from PIL import Image
#FIXME remove dependency
import numpy as np

# create a big image > 2gb in memory
size = 15000
buff = np.random.randint(0, 256, (size, size, 3))
im = Image.frombuffer('RGB', (size, size), buff, 'raw', 'RGB', 0, 1)

assert (im.size == (size, size))
#assert len(im.tobytes()) == 1300

print('ok')
