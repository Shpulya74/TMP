class FruitsVisitor(object):
    """Посетитель"""
    def draw(self, fruits):
        methods = {
            Banana: self.draw_banana,
            Apple: self.draw_apple,
        }
        draw = methods.get(type(fruits), self.draw_unknown)
        draw(fruits)
 
    def draw_banana(self, fruits):
        print ('Банан')
 
    def draw_apple(self, fruits):
        print ('Яблоко')
 
    def draw_unknown(self, fruits):
        print ('Фрукт')
 
class Fruits(object):
    def draw(self, visitor):
        visitor.draw(self)
 
class Banana(Fruits):
    """Банан"""
 
class Apple(Fruits):
    """Яблоко"""
 
class Orange(Fruits):
    """Апельсин"""
 
visitor = FruitsVisitor()
 
banana = Banana()
banana.draw(visitor)
 
apple = Apple()
apple.draw(visitor)
 
orange = Orange()
orange.draw(visitor)