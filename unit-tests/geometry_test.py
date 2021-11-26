#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:15:35 2019

@author: psakievich
"""
from geometry import *

def test_LineSegmentConstructsFromTwoPoints():
    a = [0, 1]
    b = [1, 0]
    line = LineSegment(a,b)
    assert isinstance(line, Geometry)
    assert line.p1 == a
    assert line.p2 == b