from math import *
start_points = []
final_points = []

height = 1
for i in range(100):
    height += 0.2
    start_points.append([2, round(height,1)])

print(start_points)

height = 3
for i in range(25):
    height += 0.2
    final_points.append([6, round(height,1)])


height = 6
for i in range(25):
    height += 0.2
    final_points.append([round(height,1), 8.2])


height = 8.2
for i in range(25):
    height -= 0.2
    final_points.append([11, round(height,1)])


height = 11
for i in range(25):
    height -= 0.2
    final_points.append([round(height,1), 3])

print(final_points)

print(len(start_points))
print(len(final_points))
