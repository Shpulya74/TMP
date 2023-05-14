from abc import ABC, abstractmethod

class Algorithm(ABC):

    def template_method(self):

        self.sport()
        self.work()
        self.home()
        self.child()
        self.final()
        self.printer()

    def sport(self):
        print("Сделать утреннюю зарядку")

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def home(self):
        pass

    @abstractmethod
    def child(self):
        pass

    def final(self):
        print('Распорядок на три дня составлен')

    def printer(self):
        n = 50
        print("-" * n)
class menu:
    def table(self):
        print("Составить таблицу с графиком работы")

    def sobes(self):
        print("Провести собеседование")

    def otchet(self):
        print("Составить квартальный отчёт")

    def stirka(self):
        print("Постирать вещи")

    def photo(self):
        print("Разложить фотографии по альбомам")

    def english(self):
        print("Отвести дочь на занятия по английскому")

    def doctor(self):
        print("Сходить к педиатру")

    def cinema(self):
        print("Сходить на мультфильм")

    def cake(self):
        print("Приготовить торт для свекрови")

    def window(self):
        print("Помыть окно в спальне")

    def book(self):
        print("Почитать дочери сказку")

    def korp(self):
        print("Устроить корпоратив")

class Monday(Algorithm):
    def work(self):
        z = menu()
        z.table()

    def home(self):
        z = menu()
        z.stirka()

    def child(self):
        z = menu()
        z.english()

    def final(self):
        print('Распорядок дня на пн составлен')

class Tuesday(Algorithm):
    def work(self):
        z = menu()
        z.sobes()

    def home(self):
        z = menu()
        z.photo()

    def child(self):
        z = menu()
        z.doctor()
        z.cinema()

    def final(self):
        print('Распорядок дня на вт составлен')

class Wednesday(Algorithm):
    def work(self):
        z = menu()
        z.otchet()

    def home(self):
        z = menu()
        z.cake()
        z.window()

    def child(self):
        z = menu()
        z.english()

    def final(self):
        print('Распорядок дня на ср составлен')

print("Распорядок дня на пн")
a=Monday()
a.template_method()

print("Распорядок дня на вт")
b=Tuesday()
b.template_method()

print("Распорядок дня на ср")
c=Wednesday()
c.template_method()