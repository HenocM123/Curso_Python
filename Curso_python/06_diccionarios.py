# DICCIONARIOS #

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Henoc", "Apellido":"Maldonado", "Edad":20, 1:"python"}
my_dict = {
    "Nombre":"Henoc", 
    "Apellido":"Maldonado", 
    "Edad":20, 
    "Lenguajes":{"Python", "c++", "MySQL"},
    1: 1.69
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "carlos"
print(my_dict["Nombre"])

my_dict["Ciudad"] = "Guayaquil"
print(my_dict)

del my_dict["Ciudad"]
print(my_dict)

print("Henoc" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys((my_dict))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Henoc")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
