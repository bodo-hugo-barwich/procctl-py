'''
Definition of the `procctl` Package

@version: 2025-09-26

@author: Bodo Hugo Barwich
'''
__all__ = [
    'ProcessController',
    'ProcessGroup',
    'runProcess',
    'runProcessWithOptions']

from .controller import ProcessController
from .processgroup import ProcessGroup
from .util import *
