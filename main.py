from Box import Box
import os

def Select(player: Box):
    sec = input("Enter your selection [from '01' to '25']:- ")
    player.cross_element(sec)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def row_counter(player: Box):
    bingo_string = {1: "B", 2: "I", 3: "N", 4: "G", 5: "O"}
    rl = player.RowLined()
    res = []
    for i in rl:
        if rl[i] == True:
            res.append(i)

    out = ""
    for i in res:
        out+=bingo_string[i]
    
    return out

def column_counter(player: Box):
    bingo_string = {1: "B", 2: "I", 3: "N", 4: "G", 5: "O"}
    rl = player.ColumnLined()
    res = []
    for i in rl:
        if rl[i] == True:
            res.append(i)

    out = ""
    for i in res:
        out+=bingo_string[i]
    
    return out

def Result(player: Box, rc, cc):
    h = rc(player)
    v = cc(player)

    res = h + v
    res = list(set(res))

    return res


def main():

    P1 = Box()

    while True:

        rc = row_counter
        cc = column_counter
        res = Result(P1, rc, cc)

        if not P1.box_finish():
            clear()
            print()
            print("=="*20)
            print()
            print(P1)
            print("=="*20)
            # print(cc)
            print(res)
            Select(P1)

        else:
            print(P1)
            # print(cc)
            print(res)
            break
    
        

if __name__ == "__main__":
    main()
