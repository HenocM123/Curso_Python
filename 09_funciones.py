# Funciones #

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_number, second_number):
   my_sum = first_number + second_number
   return my_sum

sum_two_values(5, 6)
sum_two_values(523, 121)
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(name="Henoc", surname="Maldonado")
print_name(surname="Maldonado", name="Henoc")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Henoc", "Maldonado")
print_name_with_default("Henoc", "Maldonado", "HenocM123")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "python", "HenocM123")
print_upper_texts("Hola")

