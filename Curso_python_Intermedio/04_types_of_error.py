# types of error #
"Quitar el # y ejecutar para identifcar el error"

# SyntaxError
# print "¡Hola Comunidad!"  # Descomentar para Error
print("¡Hola Comunidad!")

# NameError
# print(other_language) # Descomentar para Error
language = "spanish"
print(language)

# IndexError
my_list = ["Python", "Swift", "kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

#ModuleNotFoundError
# import maths  # Descomentar para Error
import math

# AtributeError
# print(math.PI)    # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Henoc", "Apellido": "Maldonado","Edad":20}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error

# TypeError
#print(my_list["0"])    # Descomentar para Error
print(my_list[0])
print(my_list[False]) #no es recomendable
print(my_list[True]) #no es recomendable

# ImportError
#from math import PI    # Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 años")    # Descomentar para Error
my_int = int("10") 
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para Error
print(4/2)