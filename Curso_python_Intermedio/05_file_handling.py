# File Handling #

import os

txt_file = open("Curso_Python_intermedio/ejemplos/my_file.txt", "w+") #Leer y escribir
txt_file.write("My name is Henoc\nMy lastname is Maldonado\nMy age is 20 years\nMy favorite language is python")

#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta kotlin")
print(txt_file.readline())

txt_file.close()

with open("Curso_Python_intermedio/ejemplos/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Switft")

#os.remove("Curso_Python_intermedio/my_file.txt")

# .json file

import json

json_file = open("Curso_Python_intermedio/ejemplos/my_file.json", "w+")


json_test = {
    "name" : "Henoc",
    "surname" : "Maldonado",
    "age" : 35,
    "languages" : ["python","java","C++"],
    "website" : "www.mi_Casa.com"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("Curso_Python_intermedio/ejemplos/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Curso_Python_intermedio/ejemplos/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv
csv_file = open("Curso_python_intermedio/ejemplos/my_file.csv", "w+")

csv.writer= csv.writer(csv_file)
csv.writer.writerow(["name", "lastname", "age", "language", "website"])
csv.writer.writerow(["Henoc", "Maldonado", 20, "Python", "www.mi_casa.com"])
csv.writer.writerow(["Juan", "", 22, "C++", ""])

csv_file.close()

with open("Curso_Python_intermedio/ejemplos/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file
#import xlrd #Debe instalarse

# .xlm file

import xml
xml_file = open("Curso_python_intermedio/ejemplos/my_file.xml", "w+")
xml_file.close()
