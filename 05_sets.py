# SETS #

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # es un dictionario {}

my_other_set = {"henoc", "maldonado", 20}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Maldonado_S.A.") # No contiene una estructura ordenada
my_other_set.add("Maldonado_S.A.") # No admite duplicados

print(my_other_set)
print("henoc" in my_other_set)
print("Henoc" in my_other_set)

my_other_set.remove("henoc")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

my_set = {"henoc", "maldonado", 20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"java", "MySQL", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({"C#", "c++"}))

print(my_new_set.difference(my_set))

print(my_new_set.intersection())
print(my_new_set)
