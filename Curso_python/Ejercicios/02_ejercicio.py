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

print("Esciba la primera palabra")
first_word = input()
print("Escriba la segunda palabra")
second_word = input()

def anagram (first_word, second_word):
    return sorted(first_word.lower()) == sorted(second_word.lower())

print(anagram(first_word, second_word))
