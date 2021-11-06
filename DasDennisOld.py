import numpy as np

def first_approach(H, m):
    # FIRST LEVEL

    first_level = np.linspace(0,1,H+1).tolist()
    print("First level: " + str(first_level))
    step_size = 1 / H
    print("Step size: " + str(step_size))

#for i in range(0, H+1):
#    print (i * step_size )

#print([i*step_size for i in range(0,H+1)])


    # SECOND LEVEL
    second_level = []
    for ind1, i in enumerate(first_level):
        #print("Value: " + str(i) + ". Index: " + str(index))
        values = [first_level[j] for j in range(len(first_level) - ind1)]
        second_level.append([[i], values])
        #print(values)
    
    for i in second_level:
        print(i)


    print("-------------------")
    # THIRD LEVEL
    third_level = []
    for ind0, i in enumerate(second_level):
        for ind1, j in enumerate(i[1]):
            #print(i[1][index])
            #print("Value: " + str([i[1][v] for v in range(len(i[1])-index)]) + ". Index: " + str(index))
            values = [first_level[v] for v in range(len(first_level)-ind1-ind0)]
            third_level.append([[i[0][0], i[1][ind1]], values])
            #print(values)
    
    for i in third_level:
        print(i)

    print("-------------------")
    # FOURTH LEVEL
    fourth_level = []
    for ind0, i in enumerate(third_level):
        for ind1, j in enumerate(i[1]):
            fourth_level.append([i[0] + [j, 1.0 - j - sum(i[0])]])

    print("N: " + str(len(fourth_level)))        
    for i in fourth_level:
        print(i)        


def get_first_level(H):
    return np.linspace(0,1,H+1).tolist()


def get_generic_level(first_level, previous_level):
    next_level = []
#    print(previous_level)
    for ind0, i in enumerate(previous_level):
        for ind1, j in enumerate(i[1]):
            values = [first_level[v] for v in range(len(first_level)-ind1-ind0)]
            next_level.append([i[0] + [i[1][ind1]], values])
    
    return next_level


def get_last_level(previous_level):
    last_level = []
    for ind0, i in enumerate(previous_level):
        for ind1, j in enumerate(i[1]):
            last_level.append([i[0] + [j, 1.0 - j - sum(i[0])]])

    return last_level


def das_dennis(H,m):
    first_level = get_first_level(H)
    previous_level = [[[],first_level]]
    for i in range(1, m-1):
        next_level = get_generic_level(first_level, previous_level)
        previous_level = next_level

    return get_last_level(previous_level)


H = 12
m = 3

weight_vectors = das_dennis(H, m)

print("Number of points: " + str(len(weight_vectors)))
for i in weight_vectors:
    print(i)
#first_approach(H, m)

"""
first_level = get_first_level(H)

a = 4
second_level = get_generic_level(first_level, [[[],first_level]])
third_level = get_generic_level(first_level, second_level)

print("Number of points: " + str(len(third_level)))
last_level = get_last_level(third_level)
for i in last_level:
    print(i)
"""

