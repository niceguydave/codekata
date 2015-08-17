#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def checkFileIsReadable(filepath):
    try:
        open(filepath)
    except IOError, OSError:  # Note OSError is for later versions of python
        raise IOError("Unable to read the supplied file '{}'".format(filepath))


def processWeather(filename):
    checkFileIsReadable(filename)
