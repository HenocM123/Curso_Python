"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""
#Preguntamos al usario las 2 palabras a usar
print("Esciba la primera palabra")
first_word = input()
print("Escriba la segunda palabra")
second_word = input()
#Comparamos si esas 2 palabras son anagramas
def anagram (first_word, second_word):
    return sorted(first_word.lower()) == sorted(second_word.lower())
#Printeamos el boolean
print(anagram(first_word, second_word))
