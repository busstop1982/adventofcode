minis = dict([(chr(i),i-96) for i in range(97,123)])
maxis = dict([(chr(i),i-38) for i in range(65,91)])
all = minis | maxis

sum = 0

with open("input",'r') as file:
    for line in file:
        splitline = list(line)
        splitline.pop(-1)
        set1 = set(splitline[len(splitline)//2:])
        set2 = set(splitline[:len(splitline)//2])
        intersection = set1 & set2
        sum += all[intersection.pop()]
print(sum)
