from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod    # esme jo method apne define keya like printar wo apko nechail prinar me define krna he
    # pdega eska yhe kaam he yha per jo function de deya usko define ka notice ayega
    # jaw ham esko inharit krenge twa he krna pdega
    # or es class ka koi object nahe bna sakti yeh bus btane ke leyai class hota he
    def printar(self):
        return 0
class area(shape) :
    def __init__(self) :
        self.lenght = 6
        self.breath = 7
    def printar(self):
        return self.lenght * self.breath

s = area()
print(s.printar())