# LOOPS #

#while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor que o igual que 10")


print("La ejecucion continua")

while my_condition <20:
    my_condition +=1
    if my_condition == 15:
        print("Mi condicion es 15")
        print("se detiene la ejecucion")
        break
    print(my_condition)

print("La ejecucion continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (20, 1.69, "Henoc", "Maldonado", "henoc")
for element in my_tuple:
    print(element)

my_set = {"Maldonado", "Henoc", 20}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Henoc", "Apellido":"Maldonado", "Edad":20}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("se ejecuta")
else:
    print("el bucle for para diccionario ah finalizado")


print("La ejecuccion continua ")