from __future__ import absolute_import, division, print_function

import time
import numpy as np

import cubao_meshcat
import cubao_meshcat.geometry as g

verts = np.random.random((3, 100000)).astype(np.float32)

vis = cubao_meshcat.Visualizer().open()
vis.set_object(g.Points(
    g.PointsGeometry(verts, color=verts),
    g.PointsMaterial()
))
