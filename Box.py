
class Box:
    """The BINGO BOX object\n
    Contains 5x5 block with numbers 1 to 25"""
    from random import shuffle
    def __init__(self):
        self.main_box = self.create_box()
        self.CD = dict.fromkeys(self.main_box, False)
        self.group_data = {"1-row": False, "2-row": False, "3-row": False, 
                                 "4-row": False, "5-row": False, "1-col": False, 
                                 "2-col": False, "3-col": False, "4-col": False, 
                                 "5-col": False, "1-dia": False, "2-dia": False
                                 }
        
        self.updater()
    
    def create_box(self):
        B = ["01","02","03","04","05",
             "06","07","08","09","10",
             "11","12","13","14","15",
             "16","17","18","19","20",
             "21","22","23","24","25"
             ]
        self.shuffle(B)
        return B
    
    def box_finish(self):
        a = [self.isCrossed(i) for i in self.main_box]
        return all(a)
    
    def updater(self):
        row_check = self.check_horizontal()
        column_check = self.check_vertical()
        diagonal_check = self.check_diagonal()

        if row_check:
            self.group_data[row_check] = True
        if column_check:
            self.group_data[column_check] = True
        if diagonal_check:
            self.group_data[diagonal_check] = True
    
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
        self.CD[Element] = True
    
    def chunk(self, lst, size):
        return [lst[i:i+size] for i in range(0, len(lst), size)]
    
    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]
    
    def check_vertical(self):
        broken_box = self.chunk(self.main_box, 5)
        nb = self.transpose(broken_box)
        counter = 1
        for i in nb:
            if self.isCrossed(i[0]) and self.isCrossed(i[1]) and self.isCrossed(i[2]) and self.isCrossed(i[3]) and self.isCrossed(i[4]):
                return f"{counter}-col"
            else:
                counter += 1
        return None
        
    
    def check_horizontal(self):
        broken_box = self.chunk(self.main_box, 5)
        counter = 1
        for i in broken_box:
                if self.isCrossed(i[0]) and self.isCrossed(i[1]) and self.isCrossed(i[2]) and self.isCrossed(i[3]) and self.isCrossed(i[4]):
                    return f"{counter}-row"
                else:
                    counter += 1
        return None
    
    def check_diagonal(self):
        mb = self.main_box
        if self.isCrossed(mb[0]) and self.isCrossed(mb[6]) and self.isCrossed(mb[12]) and self.isCrossed(mb[18]) and self.isCrossed(mb[24]):
            return f"1-dia"
        elif self.isCrossed(mb[4]) and self.isCrossed(mb[8]) and self.isCrossed(mb[12]) and self.isCrossed(mb[16]) and self.isCrossed(mb[20]):
            return f"2-dia"
        else:
            return None

    def RowLined(self):
        mb = self.chunk(self.main_box, 5)
        row_results = [all(self.isCrossed(item) for item in sublist) for sublist in mb]
        d={}
        for i in range(1,6):
            d[i] = row_results[i-1]
        return d
    