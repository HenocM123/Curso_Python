"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre 
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""
#creamos una lista
my_list = ()
#Hacemos un bucle
for my_num in range(1, 101):
    #Multiplos de 3 y 5
    print(my_num)
    if my_num % 3 == 0 and my_num % 5 == 0:
        print("fizzbuzz")
    elif my_num % 3 == 0:
        print("Fizz")
    elif my_num % 5 == 0:
        print("Buzz")