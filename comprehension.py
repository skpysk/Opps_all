
# 1 list

#s = [i for i in range(10) if i%3==0]  # list comprishension
#print(s)
# output = [1,2,3,4,] soo onn

# 2 dictionar

#{1:"item1",2:"item2"}  # so on

#dic1 = { i:f"item{i}" for i in range(100)}
#print(dic1)
# output = {0: 'item0', 1: 'item1', soo onn


#dic1 = { i:f"item{i}" for i in range(5)}
#dict2 = {value:key(# yeh new vala he) for key,value (#yha per jo old wala he wo deya he) in dic1.items()}
#print(dic1)
#print(dict2)

#{0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4'}
#{'item0': 0, 'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4} 

# 3 set comprehension

#x = { i for i in ["w1","w2","w1","w2"]}
#print(x)
# output bcz set {'w1', 'w2'}

# 4 generator comprihension

#event  = ( i for i in range(100) if i%2==0)
#print(event)
# if value lena chte he generator se to 
#print(event.__next__())  # so one all value you can get
# loop me __ next lganeke jarurat nahe he


# output <generator object <genexpr> at 0x00000233C09BA2D0>