# CLASES #

class MyEmptyPerson:  
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class MyPerson:
    def __init__(self, name, surname, alias = "sin alias"):
        self.fullname = f"{name} {surname} {alias}" #Propiedad Publica
        self._name = name    # PROPIEDAD PRIVADA
 
    def get_name (self):
        return self._name

    def walk (self):
        print(f"{self.fullname} esta caminando")

my_person = MyPerson("Henoc", "Maldonado")
print(my_person.fullname)
print(my_person.get_name())
my_person.walk()

my_other_person = MyPerson("Henoc", "Maldonado", "HenocM123")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Juan Cadena (JJ)" #es tipado debil y se lo puede variar
print(my_other_person.fullname)



class MySecondPerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  
    def savor (self):
        print(f"{self.name} esta probando la sopa")

my_second_person = MySecondPerson("Carlos", "Garcia")
my_second_person.savor()
print(f"{my_second_person.name} {my_second_person.surname}")