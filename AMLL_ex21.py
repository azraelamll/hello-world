# Ejercicio 21

def add(a,b):
    print(f"Sumando {a}+{b}")
    return a+b

def substract(a,b):
    print(f"Restando {a}-{b}")
    return a-b

def multiply(a,b):
    print(f"Multiplicando {a}*{b}")
    return a*b

def divide(a,b):
    print(f"Dividiendo {a}/{b}")
    return a/b


print("¡Hagamos algunas operaciones matemáticas sólo con funciones!")

age = add(30,5)
height = substract(1.86,0.04)
weight = multiply(45,2)
iq = divide(200,2)

print(f"Edad: {age}, altura: {height} m, Peso: {weight} kg, IQ: {iq}")

# Un acertijo para el crédito extra, escríbelo de cualquier forma.
print("Aquií está un acertijo.")

what = divide(age, multiply(height,substract(weight,add(iq, 2))))

print("Eso se convierte en: ", what, ". ¿Puedes hacerlo a mano?")
