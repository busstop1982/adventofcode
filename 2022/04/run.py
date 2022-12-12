out = 0
with open("input",'r') as file:
    for line in file:
        ranges = [i.split('-') for i in line.split(',')]#line.split(',').split('-')
        numbers = [int(item) for sublist in ranges for item in sublist]
        set1 = set(range(numbers[0],numbers[1]+1))
        set2 = set(range(numbers[2],numbers[3]+1))
        if set1.issubset(set2) or set2.issubset(set1):
            out += 1
print(out)
