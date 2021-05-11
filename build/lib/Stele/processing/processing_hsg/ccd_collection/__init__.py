__author__ = 'Sphinx'

"""
MAJOR # TODO:
Include inheritance of objects to make it actually work

Isolate where "np.set_printoptions(linewidth=500)" is utilized

complete import inside init to make code functional

The file HighSidebandCCD is in drastic need of reduction and rescoping,
likely needs to be broken down into 2, more likely 3-4 files.

rewrite code to style
"""
from . import ccd
from . import helper_functions
from . import absorbance
from . import high_sideband_ccd
from . import neon_noise_analysis
from . import photoluminescence
# from .Absorbance import *
# from .CCD import *
# from .HighSidebandCCD import *
# from .HighSidebandCCDRaw import *
# from .NeonNoiseAnalysis import *
# from .photoluminescence import *
