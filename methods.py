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
        
sonu = sonu("sonu","eng","yt") # all input
aman = sonu.from_st("aman-hindi-yot") # input app aise bhi de sakte ho
sonu.changesongnum(12)
#print(sonu.kaam)  # kya print krna he
#print(sonu.__dict__) # all variable with values
#print(sonu.kaam)
print(sonu.no_of_song) # return me new wala song num ayega
print(aman.kaam)
