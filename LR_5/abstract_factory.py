class AbstractFactory(object):

    def create_drink(self):
        raise NotImplementedError()
    
    def create_food(self):
        raise NotImplementedError()
    
class Drink(object):
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return self._name
    
class Food(object):
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return self._name
    
class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Апельсиновый сок')
    
    def create_food(self):
        return Food('Куриное филе')
    
class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Холодный чай')
   
    def create_food(self):
        return Food('Лазанья')
    
def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()
    
factory = get_factory(0)
print (factory.create_drink()) 
print (factory.create_food())