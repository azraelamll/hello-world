from sys import argv

script, filename = argv

print(f"Vamos a borrar el archivo {filename}.")
print("Si no deseas hacerlo,  presiona CTRL-C (^C).")
print("Si deseas hacerlo, presiona ENTER. ")

input("?")

print("Abriendo el archivo...")
target = open(filename, 'w')

print("Truncando el archivo. ¡Adiós!")
target.truncate()

print("Ahora te pediré que introduzcas tres líneas.")

line1 = input("Línea 1: ")
line2 = input("Línea 2: ")
line3 = input("Línea 3: ")

print("Ahora las escribiré dentro del archivo.")

target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print("Y finalmente, lo cerraré.")
target.close()
