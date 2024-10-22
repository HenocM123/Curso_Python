"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
# Definir una funcion si es o no primo
def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#Imprimir los numeros primos del 1 al 100
for num in range (1, 101):
    if primo(num):
        print(num)