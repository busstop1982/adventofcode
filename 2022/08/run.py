import numpy as np

forest = []
with open('input', 'r') as file:
    for line in file:
        forest.append([int(i) for i in line.replace('\n','')])
        
print(np.array(forest))
