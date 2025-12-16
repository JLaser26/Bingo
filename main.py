from Box import Box
import os
from random import choice
from time import sleep

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
                return a
            elif player.isCrossed(a):
                B.pop(B.index(a))
                continue
    if DF:
        return DF

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def style(text, *codes):
    return f"\033[{';'.join(codes)}m{text}\033[0m"

def flipper(a):
    while True:
        if a % 2 == 0 or a == 0:
            return 0
        elif a % 2 != 0 or a == 1:
            return 1

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

def GAME(p1: Box, p2: Box, count: int):
    if count == 0:
        f = input("Enter [0 to 25]:- ")
        player_input = f
        p1.cross_element(player_input)
        p2.cross_element(player_input)
        return f"you choosed:- {player_input}"
    elif count == 1:
        comp_input = autoSelect(p2)
        p2.cross_element(comp_input)
        p1.cross_element(comp_input)
        return f"computer choose:- {comp_input}"

def Winner(s1: str, s2: str):
    if s1 == "BINGO":
        return "PLAYER WON"
    elif s2 == "BINGO":
        return "Computer WON"
    else:
        pass

def main():

    P1 = Box()
    P2 = Box()
    count = 0

    while True:

        res1 = updater(P1)
        res2 = updater(P2)
        c = flipper(count)
        win = Winner(res1, res2)

        if not P1.box_finish() and not win:
            clear()
            print()

            print("=="*20)
            print()
            print(P1)
            print(res1)
            print("=="*20)

            g = GAME(P1, P2, c)
            print("--"*20)
            print(style(g, "1", "33"))
            print("--"*20)

            sleep(2)
            count+=1

        else:
            clear()

            print("~~"*20)
            print("YOUR BOX:- \n")
            print(P1)
            print(f"Completion -->> {res1}")
            print("~~"*20)

            if win == "PLAYER WON":
                print(style(win, "1", "32"))
            elif win == "Computer WON":
                print(style(win, "1", "31"))

            print("~~"*20)
            print("Computer's BOX:- \n")
            print(P2)
            print(f"Completion -->> {res2}")
            print("~~"*20)

            sleep(3.5)
            break    

if __name__ == "__main__":
    main()