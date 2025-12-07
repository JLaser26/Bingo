from Box import Box
import os

def Select(player: Box):
    sec = input("Enter your selection [from '01' to '25']:- ")
    player.cross_element(sec)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    P1 = Box()
    while True:
        clear()
        print()
        print("=="*20)
        print()
        print(P1)
        print("=="*20)

        Select(P1)
        if P1.box_finish():
            print(P1)
            break

if __name__ == "__main__":
    main()
