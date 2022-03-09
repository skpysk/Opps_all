#class dad :
   # pass
#class son(dad):
   # pass
#class Grandson(son):
  #  pass
 # this is multilevel inherit

class dad :
    basketball = 5
class son(dad):
    dances = 1
    def dance(self):
        return f" i am dancer {self.dances}"
class Grandson(son):
    dances = 6
    def dance(self):
        return f"yes i am dancer know  {self.dances}"

sk = dad()
pk = son()
sonu = Grandson()
print(sonu.basketball)