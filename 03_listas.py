# LISTAS #

my_list =  list()
my_other_list = []

print(len(my_list))

my_list = [20, 63, 100, 42, 20, 80, 58]
print(my_list) 
print(len(my_list))

my_other_list = [20, 1.69, "henoc", "maldonado"]
print(my_other_list)

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])
# print(my_other_list[-5]) index error por que se sale del rango

print(my_other_list.count("henoc"))
print(my_list.count(20))

age, height, name, surname = my_other_list
print(name)

print("tu nombre es:", name + "\ny tu apellido es:", surname)

print(my_list + my_other_list)
#print(my_list - my_other_list) index error

my_other_list.append("Cocacola")
print(my_other_list) 

my_other_list.insert(3, "negro")
print(my_other_list)

my_other_list[3] = "rojo"
print(my_other_list)

my_other_list.remove("rojo")
print(my_other_list)

my_list.remove(20)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[1]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "hola python"
print(my_list)
print(type(my_list))
