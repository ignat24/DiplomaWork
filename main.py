from math import *

def length_two_points(x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**1/2


start_points = [[1,1],[1, 2], [2, 2], [2, 1]]

final_points = [[5,1], [6,1], [7,1], [6,2]]

count_points = len(start_points)

length_matrix = [[], [], [], []]
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

print(length_matrix)

length_matrix = [[3,7,2,1,2], [2,1,4,7,1], [7,5,6,3,3,],[5,5,7,5,6], [1,3,2,4,7]]

for i in length_matrix:
    min_length_values.append(min(i))

print(min_length_values)

tmax = max(min_length_values)
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


   


