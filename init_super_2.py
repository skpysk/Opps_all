from pygame import init


class dad:
    song = 1
    def __init__(self):
        self.var1 = "this is dad var1"
        self.var2 = "i am var 2 from class dad"
        #self.song = "this is var 2"
class son(dad):
    song = "here"
    def __init__(self):
        self.var3 = " i am var3 here "
        super().__init__()
        print(super().song)






sonu = dad()
sharma = son()

