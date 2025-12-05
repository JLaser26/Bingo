#UNDER DEVELOPEMENT!

from random import shuffle

class Box:
    def __init__(self):
        self.main_box = self.create_box()
        self.CD = dict.fromkeys(self.main_box, False)
        self.group_data = {"1-row": False, "2-row": False, "3-row": False, 
                                 "4-row": False, "5-row": False, "1-col": False, 
                                 "2-col": False, "3-col": False, "4-col": False, 
                                 "5-col": False, "1-dia": False, "2-dia": False
                                 }
    
    def create_box(self):
        B = ["01","02","03","04","05",
             "06","07","08","09","10",
             "11","12","13","14","15",
             "16","17","18","19","20",
             "21","22","23","24","25"
             ]
        shuffle(B)
        return B
    
    def __repr__(self):
        counter = 1
        res = ""
        for i in self.main_box:
            if counter % 5 == 0:
                if not self.isCrossed(i):
                    res+=f"| {i} |"
                    counter += 1
                elif self.isCrossed(i):
                    res += f"| \033[9;31m{i}\033[0m |"
                    counter += 1
                res += "\n"
            else:
                if not self.isCrossed(i):
                    res+=f"| {i} |"
                    counter += 1
                elif self.isCrossed(i):
                    res += f"| \033[9;31m{i}\033[0m |"
                    counter += 1
        return res
    
    def isCrossed(self, Element: str) -> bool:
        return self.CD[Element] == True
    
    def cross_element(self, Element: str):
        if self.CD[Element] == True:
            return None
        else:
            self.CD[Element] = True
    
    def chunk(self, lst, size):
        return [lst[i:i+size] for i in range(0, len(lst), size)]

    
    def check_vertical(self):
        ...
    
    def check_horizontal(self):
        broken_box = self.chunk(self.main_box, 5)
        counter = 1
        for i in broken_box:
            if self.isCrossed(i[0]) and self.isCrossed(i[1]) and self.isCrossed(i[2]) and self.isCrossed(i[3]) and self.isCrossed(i[4]):
                return f"{counter}-row"
            else:
                counter += 1


#TESTING:-
X = Box()

while True:
    print(X)
    inp = input("Enter:- ")
    X.cross_element(inp)
