# STRINGS #

my_string = "mi string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + "hola " + my_other_string)

my_new_line_string = "este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\t este es un string con tabulacion"
print(my_tab_string)

my_escape_string = "\\t este es un String \n escapado"
print(my_escape_string)


# formateo #

name, surname, age = "Henoc", "Maldonado", 20
print("mi nombre es: {} {} y mi edad es de {}".format(name, surname, age))
print("mi nombre es: %s %s y mi edad es de %d" %(name, surname, age))
print(f"mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres #
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División #
language_slice = language[1:4]
print(language_slice)

language_slice = language[0:6]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reversa #
reversed_language = language[::-1]
print(reversed_language)

# Funciones #

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
