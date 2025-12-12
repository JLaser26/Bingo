from Box import Box
import os

def Select(player: Box):
    sec = input("Enter your selection [from '01' to '25']:- ")
    player.cross_element(sec)

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

def main():

    P1 = Box()

    while True:

        rc = row_counter
        cc = column_counter
        dc = diagonal_counter
        res = Result(P1, rc, cc, dc)

        if not P1.box_finish():
            clear()
            print()
            print("=="*20)
            print()
            print(P1)
            print("=="*20)
            print(res)
            Select(P1)

        else:
            print(P1)
            print(res)
            break    

if __name__ == "__main__":
    main()