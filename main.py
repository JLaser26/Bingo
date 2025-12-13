from Box import Box
import os
from random import choice

def Select(player: Box):
    sec = input("Enter your selection [from '01' to '25']:- ")
    if player.isCrossed(sec):
        print("Already crossed try again!")
    else:
        player.cross_element(sec)

#Tested and works fine!
def autoSelect(player: Box, DF = None):
    B = [    "01","02","03","04","05",
             "06","07","08","09","10",
             "11","12","13","14","15",
             "16","17","18","19","20",
             "21","22","23","24","25"
             ]
    if not DF:
        while True:
            a = choice(B)
            if not player.isCrossed(a):
                player.cross_element(a)
                break
            elif player.isCrossed(a):
                B.pop(B.index(a))
                continue
    if DF:
        player.cross_element(DF)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def row_counter(player: Box):
    rl = player.RowLined()
    res = []
    for i in rl:
        if rl[i] == True:
            res.append(i)

    return res

def column_counter(player: Box):
    rl = player.ColumnLined()
    res = []
    for i in rl:
        if rl[i] == True:
            res.append(i)

    return res

def diagonal_counter(player: Box):
    dl = player.DiagonalLined()
    res = []
    for i in dl:
        if dl[i] == True:
            res.append(i)
    
    return res

def Result(player: Box, rc, cc, dc):
    point_table = {0: "*", 1: "B", 2: "BI", 3: "BIN", 4: "BING", 5: "BINGO"}
    h = rc(player)
    v = cc(player)
    d = dc(player)

    ml = h+v+d
    point = 0
    for _ in ml:
        point+=1    
    
    if point <= 5:
        return point_table[point]
    elif point > 5:
        return point_table[5]

def updater(P: Box):
    rc = row_counter
    cc = column_counter
    dc = diagonal_counter
    res = Result(P, rc, cc, dc)

    return res

def main():

    P1 = Box()
    P2 = Box()

    while True:

        res1 = updater(P1)
        res2 = updater(P2)

        if not P1.box_finish():
            clear()
            print()
            print("=="*20)
            print()
            print(P1)
            print("=="*20)
            print(res1)
            Select(P1)

        else:
            print(P1)
            print(res1)
            break    

if __name__ == "__main__":
    main()