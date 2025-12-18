
class Box:
    """\n
    Contains 5x5 block with numbers 01 to 25
    """

    from random import shuffle
    
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
        self.shuffle(B)
        return B
    
    def box_finish(self):
        a = [self.isCrossed(i) for i in self.main_box]
        return all(a)
    
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

    def diagonals(self, matrix):
        n = len(matrix)
        primary = [matrix[i][i] for i in range(n)]
        secondary = [matrix[i][n - 1 - i] for i in range(n)]
        return primary, secondary
    
    def DiagonalLined(self):
        mb = self.chunk(self.main_box, 5)
        d1, d2 = self.diagonals(mb)
        dd = [d1, d2]
        row_results = [all(self.isCrossed(item) for item in sublist) for sublist in dd]
        d={}
        for i in range(1,3):
            d[i] = row_results[i-1]
        return d     

    def RowLined(self):
        mb = self.chunk(self.main_box, 5)
        row_results = [all(self.isCrossed(item) for item in sublist) for sublist in mb]
        d={}
        for i in range(1,6):
            d[i] = row_results[i-1]
        return d
    
    def ColumnLined(self):
        mb = self.transpose(self.chunk(self.main_box, 5))
        row_results = [all(self.isCrossed(item) for item in sublist) for sublist in mb]
        d={}
        for i in range(1,6):
            d[i] = row_results[i-1]
        return d