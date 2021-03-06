﻿import numpy as np
import matplotlib.pyplot as plt
import math2d

from mesh import continuous_path_order

class Solid(object):
    def __init__(self, mesh, inner_material, outer_material):
        self.mesh = mesh
        self.inner_materials = np.tile(inner_material, np.size(self.mesh.segments, 0))
        self.outer_materials = np.tile(outer_material, np.size(self.mesh.segments, 0))
        self.color = inner_material.color
    
    def draw(self, draw_normals=False):
        #segments = continuous_path_order(self.mesh.segments)
        segments = self.mesh.segments

        xs = np.ravel(segments[:, :, 0])
        ys = np.ravel(segments[:, :, 1])

        plt.fill(xs, ys, color=self.color)

        if draw_normals:
            for segment in segments:
                normal = math2d.normal(segment)
                center = math2d.center(segment)
                plt.arrow(center[0], center[1], normal[0], normal[1], width=0.01, color=self.color)