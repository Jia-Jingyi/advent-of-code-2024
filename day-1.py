import numpy as np

list_1 = []
list_2 = []
count = 0

with open('input.txt','r') as file:
    for line in file:
        split_list = line.split()
        list_1.append(int(split_list[0]))
        list_2.append(int(split_list[1]))


similarity_score = 0
for num in list_1:
    similarity = list_2.count(num)
    similarity_score = similarity_score + (num * similarity)

print(similarity_score)

list_1.sort()
list_2.sort()

list_1 = np.array(list_1)
list_2 = np.array(list_2)


distance = np.subtract(list_1,list_2)

sum_distance = 0
for n in distance:
    sum_distance = sum_distance + abs(n)

print(sum_distance)

