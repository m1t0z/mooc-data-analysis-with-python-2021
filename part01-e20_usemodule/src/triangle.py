#!/usr/bin/env python3
"""Triangle helper routines"""

__author__ = "Someone"
__version__ = "0.1"

import math


def hypothenuse(a, b):
    """Calculate hypothenuse"""
    return math.sqrt(a**2 + b**2)


def area(a, b):
    """Calculate area"""
    return a * b / 2
