calories = []
with open("numbers", 'r') as f:
    value = 0
    for line in f:
        if line != "\n":
            value += int(line)
        else:
            calories.append(value)
            value = 0
calories.sort()
print(calories[-1]+calories[-2]+calories[-3])
