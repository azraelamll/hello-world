# Ejercicio 20

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("Primero, visualicemos el archivo entero:\n")

print_all(current_file)

print("Ahora, rebobinemos, como si fuera una cinta.")

rewind(current_file)

print("Imprimamos tres líneas:")

current_line = 1
while current_line <= 3:
    print_a_line(current_line, current_file)
    current_line+=1

