"""TODO"""
try:
    __FITTER_FIT_FUNCTIONS_IMPORTED__
except NameError:
    __FITTER_FIT_FUNCTIONS_IMPORTED__= False

if not __FITTER_FIT_FUNCTIONS_IMPORTED__:
    from .generic_fitter import GenericFitter, GenericFitterTool
    from .linear import LineTool
    from .quadratic import QuadraticTool
    from .exponential import ExponentialTool
    from .gaussian import GaussianTool
    from .trigonometric import TrigonometricTool
    
__FITTER_FIT_FUNCTIONS_IMPORTED__ = True