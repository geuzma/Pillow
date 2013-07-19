from tester import *

from PIL import Image
from PIL import ImageFile

codecs = dir(Image.core)

if "jpeg_encoder" not in codecs or "jpeg_decoder" not in codecs:
    skip("jpeg support not available")

# sample jpeg stream
file = "Images/lena.jpg"
data = open(file, "rb").read()

def roundtrip(im, **options):
    out = BytesIO()
    im.save(out, "JPEG", **options)
    bytes = out.tell()
    out.seek(0)
    im = Image.open(out)
    im.bytes = bytes # for testing only
    return im

def test(n):
    # The ICC APP marker can store 65519 bytes per marker, so
    # using a 4-byte test code should allow us to detect out of
    # order issues.
    icc_profile = (b"Test"*int(n/4+1))[:n]
    assert len(icc_profile) == n # sanity
    im1 = roundtrip(lena(), icc_profile=icc_profile)
    improfile = im1.info.get("icc_profile")
    print ('#### profile: ', improfile)
    assert_equal(improfile, icc_profile or None)
test(4)
