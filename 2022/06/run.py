with open("input", 'r') as file:
    for line in file:
        for i in range(0,len(line)):
            block = set(line[i:i+14])
            if len(block) == 14:
                print(i+14)
                break
            
