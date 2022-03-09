# khud ka kuch print kregalike sirf good morning bolna he to 

class sonu :
    no_of_song = 10
    def __init__(self,nam,job,stu):
        self.name = nam
        self.kaam = job
        self.study = stu
    @classmethod
    def changesongnum(cls,newsong):  # yeh new song ko return krega jo ke class ko he change ker dega
        cls.no_of_song = newsong
    @classmethod
    def from_st(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))  # upper waleka alternative
    @staticmethod
    def print(string):
        print("good morning "+ string)   # esko class se koi matlove nahe hota bus esko ek string mela or khtam
        #return "thank you"  # none ayega usko htana he  # ager nahe dena he to simple print mat kro only func ko input dedo like 29 line
sonu = sonu("sonu","eng","yt") # all input
aman = sonu.from_st("aman-hindi-yot") # input app aise bhi de sakte ho
sonu.changesongnum(12)
#print(sonu.kaam)  # kya print krna he
#print(sonu.__dict__) # all variable with values
#print(sonu.kaam)
print(sonu.no_of_song) # return me new wala song num ayega
print(aman.kaam)
sonu.print("sonu") # static ko yha se input or out leya he # yha per Employee bhi de sakti ho Employee.print("sonu")