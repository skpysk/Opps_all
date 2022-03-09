class Employee:
    num_of = 8
    def __init__(self,xname,xsalary): # how many variables do yo have name salary or more
        self.name = xname # xname alg he yeh input ke toor per jayega or self.name wala wo alg he
        self.salary = xsalary
        
    def PrintDetailes(self):
        return f"your name is {self.name} and salary is {self.salary}" # self yhe krta he aman ko yha tak lata he jo ke udher se send keya gya
        # self ke jgha per khud se yeh instance variable le lega like aman self per a jayega

sonu = Employee("sonu","35k")# init ke bad hmko yha se variable ke value dene he input ke toor per
#aman = Employee()
# yeh kamm ab nechai wala initker dega
#sonu.name = "sonu"
#sonu.salary = "35k"
#aman.name = "aman"  # yha per ham saw kuch lekh rhe he like sonu.name fer uska "sonu" or yhe cheej comon he aman me bhi to
 # kyu na ham sirf name he de "sonu" to uske leyai init ka use hota he
#aman.salary = "40k"

#print(aman.PrintDetailes()) # yhe se aman ja chuka he self ke jga per es leyai 1 was given ara he
print(sonu.name) # or app init or func me jo value de the usko yha se print kra sakte ho