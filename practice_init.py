class sonu :
    def __init__(self,nam,job,stu):
        self.name = nam
        self.kaam = job
        self.study = stu
        
sonu = sonu("sonu","eng","yt") # all input
print(sonu.kaam)  # kya print krna he
print(sonu.__dict__) # all variable with values
print(sonu.kaam)