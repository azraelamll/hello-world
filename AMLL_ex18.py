# Ejercicio 18


# este es como tus scripts con argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# OK, ese *args en realidad es inútil, podemos hacer simplemente esto
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# este solo toma un argumento
def print_one(arg1):
    print(f"arg1: {arg1}")

# este no coma argumentos
def print_none():
    print("no tengo nada.")
    
print_two("Andre", "Marcel")
print_two_again("Andre", "Marcel")
print_one("¡Primero!")
print_none()
