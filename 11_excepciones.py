# Excepciones #

numberOne = 5
numberTwo = 1
numberTwo = "1"


# try except 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #se ejecuta si se produce un error
    print("Se ha producido un error")


# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecucion continúa correctamente")


# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecucion continúa correctamente")
finally:
    print("La ejecución continua")


# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    #se ejecuta si se produce de tipo TyperError
    print("Se ha producido un TypeError")
except ValueError:
    #se ejecuta si se produce de tipo ValueError
    print("Se ha producido un ValueError")


# Captura de la informacion de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
