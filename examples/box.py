from __future__ import absolute_import, division, print_function

import math
import time

import cubao_meshcat

vis = cubao_meshcat.Visualizer().open()

box = cubao_meshcat.geometry.Box([0.5, 0.5, 0.5])
vis.set_object(box)

draw_times = []

vis["/Background"].set_property("top_color", [1, 0, 0])

for i in range(200):
    theta = (i + 1) / 100 * 2 * math.pi
    now = time.time()
    vis.set_transform(cubao_meshcat.transformations.rotation_matrix(theta, [0, 0, 1]))
    draw_times.append(time.time() - now)
    time.sleep(0.01)

print(sum(draw_times) / len(draw_times))


