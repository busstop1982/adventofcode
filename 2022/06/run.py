with open("input", 'r') as file:
    for line in file:
        for i in range(0,len(line)):
            block = set(line[i:i+4])
            #print(line[i:i+3],block)
            if len(block) == 4:
                print(i+4)
                break
            
