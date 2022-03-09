from functools import lru_cache
import functools
import time


@functools.lru_cache(maxsize=4) # 4 ka mtlove hai 4 value ko he cash krega jetna man utna ker sakte ho
def myfunc(x):
    time.sleep(2)
    return x

myfunc(1) 
# myfunc(1) takes 2 seconds and results for myfunc(1) are now cached
myfunc(1)
print("hello")
myfunc(2)
myfunc(3)
myfunc(4)
myfunc(5)  # function ko ek output nekalneme ketna time lga uske output ko record ker
# leya jata he or fer again jaw koi same input per output lena chta heto usko pehle he record ker ke rkh leya jata
# # hai take time na lge or optimize ho jaye programe or function 