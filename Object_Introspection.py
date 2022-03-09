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
# object introspection object ke pure detail ko bolte usje kya class he kes type ka he 

# tpe("")
#id("")
#dict() # saw kuch bta dega yeh object ka