from itertools import islice

minis = dict([(chr(i),i-96) for i in range(97,123)])
maxis = dict([(chr(i),i-38) for i in range(65,91)])
all = minis | maxis

sum = 0

with open("input",'r') as file:
    while True:
        lines_gen = list(islice(file, 3))
        if not lines_gen:
            break
        foo = set()
        for line in lines_gen:
            bar = set(line)
            bar.discard('\n')
            if foo.isdisjoint(bar):
                foo = foo | bar
            else:
                foo = foo & bar
        print(foo)
        sum += all[foo.pop()]
print(sum)
