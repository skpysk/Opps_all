# ek class dusre class se linked he single

class Employee :
    no_of_song = 10
    def __init__(self,nam,job,stu, ext):
        self.name = nam
        self.kaam = job
        self.study = stu
        self.ext = ext
    def printdet(self):
        return f"the name is {self.name} and kaam is {self.kaam} or study is {self.study}  or ext"
    @classmethod
    def changesongnum(cls,newsong):  # yeh new song ko return krega jo ke class ko he change ker dega
        cls.no_of_song = newsong
    @classmethod
    def from_st(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def print(string):
        print("good morning "+ string)
class Peogrammer(Employee):   # init eska he lekin jo upper he pehli se he like name or more so hmko fer se lekhi ne ke jrurat nhe he
    #es leyai super init ka use hota he bcz copy na krna pde but kuch or bhi add ker sakte ho  arguments pass krna pdega
    def __init__(self, nam, job, stu,languages):
        self.name = nam
        self.kaam = job
        self.study = stu
        self.languages = languages
    def printde(self):
        return f"programmer name is {self.name} and kaam {self.kaam} uska rool {self.study} languages are {self.languages}"
        
sonu = Employee("sonu","eng","yt","ext yha") 
#aman = sonu.from_st("aman-hindi-yot")

shubam = Peogrammer("shubham kumar","programmer","no pro in program",["python","c"])

print(shubam.printde()) # esme employee ke sabhi func bhi run ho sakti he bcz single inhetit