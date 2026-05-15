# 8-m
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Yosh xato")
          
a1 = Animal("Sher", 5)
print(a1.get_age())
a1.set_age(7)
print(a1.get_age())

a1.set_age(-2)
