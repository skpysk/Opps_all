# ek class dusre class se linked he single
# 2 class kesi 3 class se link hoga multilavel

from unicodedata import name


class Employee :
    no_of_song = 10
    def __init__(self,nam,job,stu, ext):
        self.name = nam
        self.kaam = job
        self.study = stu
        self.ext = ext
    def printdet(self):
        return f"the name is {self.name} and kaam is {self.kaam} or study is {self.study}  or ext"

class player :
    def __init__(self,name,game):
        self.name = name
        self.games = game
    def playerdet(self):
        return f"the name is {self.name} and kaam is {self.games}"
class coolprogramemmer(Employee,player):
    lang = "c"
    def printpdet(self):
        print(self.lang)
        
sonu = Employee("sonu","eng","yt","ext yha") 

shubam = player("shubam","cricket") # player class ko he def hoga run
sharma = coolprogramemmer("sharma","cricket","stu", "ext") # class cool ka def he run hoga

print(sharma.printdet())