#!/usr/bin/python3
# -*- coding: utf-8 -*-
##===-----------------------------------------------------------------------------*- Python -*-===##
##
##                                   S E R I A L B O X
##
## This file is distributed under terms of BSD license. 
## See LICENSE.txt for more information.
##
##===------------------------------------------------------------------------------------------===##
##
## Setup serialboxC library.
##
##===------------------------------------------------------------------------------------------===##

from .common import get_library

lib = get_library()

def init_serialbox():
    """Initialize the SerialboxC library by installing the error handler.
    """
    lib.serialboxInstallFatalErrorHandler(lib.serialboxStateErrorHandler)
    print("init serialbox")

init_serialbox()

