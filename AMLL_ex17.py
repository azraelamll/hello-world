from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiando desde el archivo {from_file} hacia el archivo {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"El archivo de entrada mide {len(indata)} bytes.")

print(f"¿Existe el archivo de salida {exists(to_file)}")
print("Listo. Presiona ENTER para continuar. CTRL-C para abortar.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Bien, finalizado")

out_file.close()
in_file.close()
