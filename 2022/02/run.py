class hand:
    def __init__(self, name):
        if name == 'A' or name == 'X':
            self.name = 'rock'
            self.value = 1
        if name == 'B' or name == 'Y':
            self.name = 'paper'
            self.value = 2
        if name == 'C' or name == 'Z':
            self.name = 'scissor'
            self.value = 3

    def __gt__(self, other):
        if self.name == 'rock':
            if other.name == 'scissor':
                return True
            if other.name == 'paper':
                return False
        if self.name == 'paper':
            if other.name == 'rock':
                return True
            if other.name == 'scissor':
                return False
        if self.name == 'scissor':
            if other.name == 'paper':
                return True
            if other.name == 'rock':
                return False

    def __eq__(self, other):
        return self.name == other.name

def score(enemy: hand, me: hand) -> int:
    winscore = 0
    if enemy == me:
        winscore = 3
    if me>enemy:
        winscore = 6

    return me.value + winscore

myscore = 0

with open("rps",'r') as file:
    for line in file:
        adv = line.split()
        enemy = hand(adv[0])
        me = hand(adv[1])
        myscore += score(enemy,me)

print(myscore)
