from math import *

def length_two_points(x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**1/2

start_points_9 = [[1,3],[1,4], [1,5], [1, 5.5], [1,6.5],[1,7], [2, 6.5], [2.5, 6], [2, 5.5]]
final_points_9 = [[7,3],[7,5], [7,7], [8, 6], [8.5,5],[9,6], [10, 7], [10, 5], [10, 3]]

start_points = [[1,1],[1, 2.5], [1.5, 2], [2, 2.5],[2,1]]

final_points = [[4.5,1.5], [5,1], [5.5,1.5], [5.5,2], [5,2.5]]

count_points = len(start_points)
length_matrix = []
for i in range(count_points):
    length_matrix.append([])

min_length_values = []

for i in range(count_points):
    x1 = start_points[i][0]
    y1 = start_points[i][1]
    for j in range(count_points):
        x2 = final_points[j][0]
        y2 = final_points[j][1]
        distance = length_two_points(x1, y1, x2, y2)
        # print(distance)
        length_matrix[j].append(distance)

    # print("next")


for i in range(count_points):
    print(length_matrix[i])

# length_matrix = [[3,7,2,1,2], [2,1,4,7,1], [7,5,6,3,3,],[5,5,7,5,6], [1,3,2,4,7]]

for i in length_matrix:
    min_length_values.append(min(i))
print()
print(min_length_values)

tmax = max(min_length_values)
print()
print(tmax)

for i in range(len(length_matrix)):
    tmax = max(min_length_values)
    # print(length_matrix)
    index_finish = min_length_values.index(tmax)
    # index_start = length_matrix[index_finish].index(tmax)
    try:
        index_start = length_matrix[index_finish].index(tmax)
    except:
        tmax = min(length_matrix[index_finish])
        index_start = length_matrix[index_finish].index(tmax)
    

    print(f"X{str(index_start+1)} --> X{str(index_finish + 1)}, distance = {tmax}")
    
    min_length_values[index_finish] = 0
    for i in range(count_points):
        length_matrix[i][index_start]= 10000


   


