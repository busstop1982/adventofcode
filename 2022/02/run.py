class hand:
    def __init__(self, name):
        if name == 'A' or name == 'rock':
            self.name = 'rock'
            self.value = 1
            self.loose = 'paper'
            self.win = 'scissor'
        if name == 'B' or name == 'paper':
            self.name = 'paper'
            self.value = 2
            self.loose = 'scissor'
            self.win = 'rock'
        if name == 'C' or name == 'scissor':
            self.name = 'scissor'
            self.value = 3
            self.loose = 'rock'
            self.win = 'paper'

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
        #i gotta loose
        if adv[1] == 'X':
            myhand = hand(enemy.win)
        #i gotta tie
        if adv[1] == 'Y':
            myhand = hand(enemy.name)
        #i gotta win
        if adv[1] == 'Z':
            myhand = hand(enemy.loose)
        myscore += score(enemy,myhand)

print(myscore)
