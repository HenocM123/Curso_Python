"""
Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...

"""

#Definir la funcion fibonacci
def fibonacci(num):
    #El numero empieze desde 0
    if num < 2:
        return num
    else:
        #Formula de fibonacci
        return fibonacci(num-1) + fibonacci(num-2)

for x in range(51): #Imprime los numeros que nos pide en el caso dice los 50 primeros numeros
    print(fibonacci(x))

"""
#Esta es una forma de hacerlo mas eficiente y demora menos para evitar recalculos

def fibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num < 2:
        return num
    memo[num] = fibonacci(num-1, memo) + fibonacci(num-2, memo)
    return memo[num]

for x in range(51):  # Imprime los primeros 50 números de Fibonacci
    print(fibonacci(x))

"""