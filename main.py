from Box import Box
import os

def Select(player: Box):
    sec = input("Enter your selection [from '01' to '25']:- ")
    player.cross_element(sec)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def BINGO_COUNTER(player: Box):
    d = {0: None, 1: "B", 2: "BI", 3: "BIN", 4: "BING", 5: "BINGO"}
    res = 0
    if player.check_vertical(): res += 1
    if player.check_horizontal(): res += 1
    if player.check_diagonal(): res += 1

    return d[res]

def row_counter(player: Box):
    rl = player.RowLined()
    res = ""
    for i in rl:
        if rl[i] == True:
            res += str(i) + ", "
        else:
            continue
    return res

def main():
    P1 = Box()
    c=0
    while True:
        rc = row_counter(P1)
        clear()
        print()
        print("=="*20)
        print()
        print(P1)
        print("=="*20)
        print(rc)
        

        Select(P1)
        if P1.box_finish():
            print(P1)
            break

if __name__ == "__main__":
    main()
