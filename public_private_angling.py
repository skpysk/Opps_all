# public -  normal jo use jota he
# protect - jesko aap btao gee wo he use krega  # koi class or chil class ke alawa enka use ne ker payega
# private - only you can use _class__private

class Employee :
    no_of_song = 10
    __var = 5
    def __init__(self,nam,job,stu):
        self.name = nam
        self.kaam = job
        self.study = stu
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
        
sonu = Employee("sonu","eng","yt") 

#shubam = player("shubam","cricket") # player class ko he def hoga run
#sharma = coolprogramemmer("sharma","cricket","stu", "ext") # class cool ka def he run hoga

print(sonu._Employee__var)