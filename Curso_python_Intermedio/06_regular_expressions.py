# Regular expressions #

import re
my_string = "Esta es la leccion numero 7: leccion llamada en Expresiones regulares"
my_other_string = "Esta no es la leccion numero6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = print(re.match("Esta no es la leccion", my_other_string))
#if not(match == None):
#if match is not None:
if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

#search
search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("Expresiones regulares", "RegEX", my_string))
print(re.sub("[l|L]eccion", "LECCION", my_string))

# Patterns

pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))

pattern = r"[lL]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # El numero
print(re.findall(pattern, my_string))

pattern = r"\D" # las letras
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "henoc@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "henoc@gmail.es"
print(re.findall(pattern, email))


