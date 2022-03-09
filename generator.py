# 1 iterable  -   __iter__ ()or __getitem__   apk edher se udher ker sakte ho like sonu oso
# 2 iterator -    __next__()
# 3 iteration -   __




def gen(n):
    for i in range(n):
        yield i

d = gen(5)
print(d)  # <generator object gen at 0x000002232FDEA730> eska matlobe he es location per yeh all
# number generat ho gya he es number ke under saw kuch he aisa es leyai krte he kyo ke ram or memory ko baccha ske
# range ek generator hai

# ab generator ke jo value hoge store jo keya uska use aise ker sakte ho

print(d.__next__())  # iterator he yha per

for i in d:
    print(i)  # for loop khud ko bnd ker leta he ya apne ko handle ker leta hai range over hone ke bad
    # generator ko ap ek bar he itrat ker sakte ho ya ek war he ka mtlove he
    # itrator value ko lekr ek war he ata he es leyai loop ka use keya hmne upper


# ab iterable 

s = "abcd"  # int ko app iterate nahe ker sakte ho 

#for i in s:
    #print(i)   # ham esko iterat ker sakte he like this kyo ke string iterable hote he 

print(iter(s)) #  <str_iterator object at 0x0000021DBBCB7CA0> yeh dega
ier = iter(s)
print(ier.__next__())
print(ier.__next__()) # ek ek ker ke print krta rhega

# int ko appp iterate nahe ker sakte ho 
