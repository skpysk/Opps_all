# pehli class ke instance self. wala khojta he khud me
# fer nahe mmela to inharit ke self. me dhundhga nahe mela to
# khud ke class me dhundhega nahe mela to 
# inharit wala class ke under dekhega 

class dad:
    song = 1
    def __init__(self):
        self.var1 = "this is dad var1"
        #self.song = "this is var 2"
class son(dad):
        var2 = "this is son var3"
sonu = dad()
sharma = son()

print(sharma.song)