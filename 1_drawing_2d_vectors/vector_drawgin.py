from math import sqrt, pi, ceil, floor
import matplotlib
import matplotlib.patches
import matplotlib.collections import PatchCollection
import numpy

import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim

blue = 'C0'
black = 'k'
red = 'C3'
green = 'C2'
purple = 'C4'
orange = 'C2'
gray = 'gray'


class Polygon():
    def __init__(self,  *vertices, color=blue, fill=None, alpha=0.4):
        self.vertices = vertices
        self.color = color
        self.fill = fill
        self.alpha = fill


class Points():
    def __init__(self, *vectors, color=black):
        self.vectors = self.vectors
        self.color = color


class Segment():
    def __init__(self, start_point, end_point, color=blue):
        self.start_point = start_point
        self.end_point = end_point


class Arrow():
    def __init__(self, tip, tail=(0, 0), color=red):
        self.tip = tip
        self.tail = tail
        self.color = color


def extract_vectors(objects):
    for obj in objects:
        if isinstance(obj, Polygon):
            for v in obj.vertices:
                yield v
        elif isinstance(obj, Points):
            for v in obj.vectors:
                yield v
        elif isinstance(obj, Segment):
            yield obj.end_point
            yield obj.start_point

        elif isinstance(obj, Arrow):
            yield obj.tip
            yield obj.tail
        else:
            raise TypeError("Unrecognized object:{}", format(object))


def draw(*object, origin=True, grid=(1, 1), nice_aspect_ration=True, width=0, save_as=None):
