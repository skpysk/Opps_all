# code me eror ane per code whe ruk jata he but ham chte he agee bde code or eror ko fix kere ya na
# na kreg but age bde to usko try exeption bolte he
# try ka mtlove he code ko try kro ya age bdo


from logging import exception


try :
    num = input()

except exception as e:  # yeh eror ko e me dal ke string ke toor per print ker dega
    print(e)
finally:   # yeh to run hoga he hoga jesa ke name he finally yeh hoga he hoga chahei code try ke under run ho ya na ho
    print()
# main use try ka yhe he ke yeh code ke eror ko print ker ke age bad jayega

try :
    num = input()
except exception as e:  
    print(e)
else:
    print() # except ya else mese koi ek run hoga ya except ya eslde
    # except nahe hoga mtlove theek se kam ker rha hai taw he
finally:
    print()  