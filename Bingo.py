#UNDER DEVELOPEMENT!

from random import shuffle, randint, choice

class Box:
    def __init__(self):
        self.main_box = self.create_box()
    
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
                res+=f"| {i} |"
                counter += 1
        return res


#TESTING:-
X = Box()
print(X)