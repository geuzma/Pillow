from tester import *
from PIL import Image

# create a big image with more than INT_MAX elt
size = 28000
buff = '\x00' * size * size * 3 
assert(len(buff) > 2 ** 32 / 2)
#print 'len buff:  ', len(buff)

im = Image.frombuffer('RGB', (size, size), buff, 'raw', 'RGB', 0, 1)
assert (im.size == (size, size))
#print 'len im  :  ', len(im.tobytes())

print('ok')
