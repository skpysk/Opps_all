from fnmatch import fnmatchcase


class Employee :
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname 
        #self.email = f"{self.fname}.{self.lname}  @gmail.com"
    def exp(self):
        return f"this employee {self.fname} {self.lname}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter  # jo func ko set krna he uska name start me den he
    def email (self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter 
    def email(self):
        self.fname = None
        self.lname = None


s = Employee("sk","pk")


s.fname = "sonu" # fname change krne ke kosish # run time me chnage kesi ho sakta he yeh reason solution ne chail hai
#  # change nahe hua es problem ko he fix krta he setter
#print(s.email())  # ab change ho jayega # ager aap () lga ker use nahe krna chte ho to 

# after property 

print(s.email) # function ko func ke trh ap use kro/na kro apke mrge he uske ke leyai apko property deco. ka use krna pdega line 11
s.fname = "pk"
s.email = "sonu.hello@email.com"  # esko set krne ke leyai he setter ka use hoga
print(s.email)

del s.email  # yeh deleter func dhundhega
print(s.email)