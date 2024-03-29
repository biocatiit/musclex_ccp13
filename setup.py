"""
Copyright 1999 Illinois Institute of Technology

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL ILLINOIS INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Illinois Institute
of Technology shall not be used in advertising or otherwise to promote
the sale, use or other dealings in this Software without prior written
authorization from Illinois Institute of Technology.
"""

## Setup file to compile the sources and install the package on your system
# ==========================================

# Build the f2py fortran extension
# --------------------------------
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

flib = Extension(name = 'ccp13',
                 extra_compile_args = ['-O3'],
                 sources = ['musclexflibs/ccp13/BGCSYM2.f', 'musclexflibs/ccp13/fitpack.f', 'musclexflibs/ccp13/sort.f',
                            'musclexflibs/ccp13/BGWSRT2.f', 'musclexflibs/ccp13/BCKSMOOTH.f', 'musclexflibs/ccp13/BLUR.f',
                            'musclexflibs/ccp13/BLURLIMITS.f']
                 )

setup(
    name='musclex_ccp13',
    version = '1.2',
    ext_modules = [flib]
)
