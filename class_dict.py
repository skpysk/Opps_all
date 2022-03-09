class Employee: 
               # saw ke leyai same he yeh
    nu_of = 8  # esme jo rhega na usa use khe bhi kabhi bhi ker sakte ho 
               #but Employee function ka name use ker ke he hoga ya usa ek object hona jrure he
    pass

sonu = Employee()  # yeh dono Employee se connect he
aman = Employee()   # aman instance he

sonu.name = "sonu"   # yeh sonu se connect he jo ke Employee se connect he
sonu.hight = "5'8"
sonu.age = "21"
aman.name = "aman"   # or yeh aman ke intance variable he
aman.hight = "5'8"
aman.age = "18"

# app sonu.name
# app Employee.num_of sabhi se excess ker sakti he
#print(Employee.nu_of)  

# ager hmko class ka Employee change krna he to hmko Emplotee uska func or . got use krna he pdeega
# example
#Employee.nu_of = 10
#print(Employee.nu_of) # pehle wala or abhi wala change ho jayega
# but jaw sonu.Employee.nu_of = 10 se change krneke ko shesh kre to nahe hoga
sonu.nu_of = 10  # yeh sonu ka intance variable he class per koi rak ne pdega
print(sonu.__dict__) # esme jetne bhi intance variable he print dict me ker dega
    # app Employee ko bhi dict ker sakti he pta chl jayega ketne he usme variable with value
