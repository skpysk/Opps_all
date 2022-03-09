import string

x = string.ascii_uppercase
y = string.ascii_lowercase
z = string.digits
r = string.punctuation

x1 = []
x1.extend(x)
x1.extend(y)
x1.extend(z)
x1.extend(r)

urpas  = input("Enter your password :  ")
s = list(urpas)
for i in s :
  for f in x1 :
     if i == f :
       print(f)
       break
