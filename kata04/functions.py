#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def checkFileIsReadable(filepath):
    try:
        open(filepath)
    except IOError, OSError:  # Note OSError is for later versions of python
        raise IOError("Unable to read the supplied file '{}'".format(filepath))
    return True


def checkFileHasValidSuffix(filepath):
    valid_extension = '.dat'
    filename, file_extension = os.path.splitext(filepath)
    if file_extension != valid_extension:
        raise ValueError("Only {} files are valid.")
    return True


def processWeather(filepath):
    checkFileIsReadable(filepath)
    checkFileHasValidSuffix(filepath)
