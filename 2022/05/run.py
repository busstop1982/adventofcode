def parse(iput:str):
    iput = iput.lstrip('move ')
    foo = iput.split('from')
    howoften = int(foo[0])
    bar = foo[1].split('to')
    origin = int(bar[0])
    goal = int(bar[1])

    return howoften, origin-1, goal-1

with open("input",'r') as file:
    n=4
    cargo = []
    for line in file:
        if "move" not in line:
            chunks = [line[i:i+n].strip('[ ]\n') for i in range(0,len(line),n)]
            if "1   2   3" not in line:
                cargo.append(chunks)
            else:
                break
    cargo.reverse()
    stacks = [[] for i in range(0,9)]
    for stack in range(0,9):
        for foo in cargo:
            if not foo[stack] == '':
                stacks[stack].append(foo[stack])
    for stack in stacks:
        print(stack)

    for line in file:
        if "move" in line:
            a,b,c = parse(line)
            for i in range(0,a):
                stacks[c].append(stacks[b].pop())
            #print(f"moved {a} thingies from {b} to {c}")
    print('done moving things:')
    for stack in stacks:
        print(stack[-1])
