# yeh problem ka solution he nechai se program execute hoga jo pehle melega yeh usi ka
# program ko kya lena he confused hojata he 


class A:
    def set(self):
        print("hello i am class A")
class B(A):
   def set(self):
        print("hello i am class B")
class C(A):
    def set(self):
        print("hello i am class C")
class D(B,C):
    pass

a = A()
b= B()
c = C()
d =D()

print(d.set())