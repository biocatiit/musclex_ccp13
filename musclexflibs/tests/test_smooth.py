import musclexflibs.ccp13.ccp13 as ccp13
# import matplotlib.pyplot as plt
import numpy as np
import fabio
# from PyQt4 import QtGui
from tifffile import imsave
import os, sys
print ccp13.bcksmooth.__doc__

img_path = os.path.split(os.path.realpath(__file__))[0] + "/test_images/July10_148.tif.result.tif"
img = fabio.open(img_path).data
width = img.shape[1]
height = img.shape[0]

img = np.ravel(img)
buf = np.array(img, 'f')
maxfunc = len(buf)
cback = np.zeros(maxfunc, 'f')
b = np.zeros(maxfunc, 'f')
smbuf = np.zeros(maxfunc, 'f')
vals = np.zeros(20, 'f')
vals[0] = fwhm = 10
vals[1] = cycles = 30
vals[2] = rmin = 20.0
vals[3] = rmax = 998.0
vals[4] = xc1 = width/2.
vals[5] = yc1 = height/2.
vals[6] = lowval = img.min()-1
vals[7] = smooth = 1.
vals[8] = tens = 1.0
vals[9] = msig = 5.0

options = np.zeros((10,10), 'S')
options[0] = ['G','A','U','S','S', '', '', '', '', '']
options[1] = ['M','E','R','G','E', '', '', '', '', '']
options = np.array(options, dtype='S')

npix = width
nrast = height
xb = np.zeros(npix, 'f')
yb = np.zeros(npix, 'f')
ys = np.zeros(npix, 'f')
ysp = np.zeros(npix, 'f')
sig = np.zeros(npix, 'f')
wrk = np.zeros(9*npix, 'f')
iflag = np.zeros(npix*nrast, 'f')
ilog = 1


ccp13.bcksmooth(buf=buf,
                cback=cback,
                b=b,
                smbuf=smbuf,
                vals=vals,
                options=options,
                xb=xb,
                yb=yb,
                ys=ys,
                ysp=ysp,
                sig=sig,
                wrk=wrk,
                iflag=iflag,
                ilog=ilog,
                nrast=nrast)

before = np.array(buf, 'float32')
before = before.reshape((height,width))
imsave("img.tif", before)

after = np.array(b, 'float32')
after = after.reshape((height,width))
imsave("bg.tif", after)

result = before-after
imsave("result_smooth.tif", result)
