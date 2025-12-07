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
        
        print(P1)
        Select(P1)
        clear()
        if P1.box_finish():
            print(P1)
            break

if __name__ == "__main__":
    main()
