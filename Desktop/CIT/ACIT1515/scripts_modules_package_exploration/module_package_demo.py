#! /usr/bin/env python3
"""
This module demonstrates the use of imports and the structure of modules and
packages
"""
# used to demonstrate reloading of a module
import importlib

# Setup Logging
from log_setup import log

# Log the start of loading this module
log("module __name__ = {} : start".format(__name__))

# import other modules
import mod1
from mod1 import mod1_global
from mod2 import mod2func
from mod3 import mod3func as myfunc
import pack1.moda
from pack1.modb import modbfunc
from pack2 import *


def main():
    """Simple demonstration of modules and packages"""

    # log the start of the main function
    log("main function start")

    mod1.mod1func()
    mod2func()
    myfunc()
    pack1.moda.modafunc()
    modbfunc()
    modc.modcfunc()
    modd.moddfunc()
    importlib.reload(mod1)

    # log the end of the main function
    log("main function end")


if __name__ == "__main__":
    main()

# log the final statement in the module
log(f"module __name__ = {__name__} : end")
