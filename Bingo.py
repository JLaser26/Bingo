#UNDER DEVELOPEMENT!

from random import shuffle

class Box:
    def __init__(self):
        self.main_box = self.create_box()
        self.CD = dict.fromkeys(self.main_box, False)
    
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
            if counter % 5 == 0 and counter != 1:
                res += "\n"
                counter += 1
            else:
                if not self.isCrossed(i):
                    res+=f"| {i} |"
                    counter += 1
                if self.isCrossed(i):
                    res += f"\033[9m| {i} |\033[0m"
                    counter += 1
        return res
    
    def isCrossed(self, Element: str) -> bool:
        return self.CD[Element] == True
    
    def cross_element(self, Element: str):
        if self.CD[Element] == True:
            return None
        else:
            self.CD[Element] = True


#TESTING:-
X = Box()
X.cross_element("20")
print(X)
