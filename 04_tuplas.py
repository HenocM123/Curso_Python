 # TUPLAS #

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.69, "henoc", "maldonado", "henoc", 53, 26, 78)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-5]) IndexError

print(my_tuple.count("Carlos"))
print(my_tuple.index("henoc"))


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[5] = "Carlos"
my_tuple.insert (1, "negro")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple