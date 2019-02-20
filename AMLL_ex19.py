# Ejercicio 19

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"¡Tienes {cheese_count} quesos!")
    print(f"¡Tienes {boxes_of_crackers} cajas de galletas!")
    print("¡Hombre, eso es suficiente para una fiesta!")
    print("Consigue una manta. \n")
    
print("Podemos darle los números a la función directamente:")
cheese_and_crackers(20,30)

print("O, podemos usar variables desde nuestro script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Inclusive podemos también hacer operaciones matemáticas:")
cheese_and_crackers(10 + 20, 5 + 6)

print("Y podemos combinar las dos, varibles y operaciones matemáticas:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Y también podemos pedirle al usuario que ingrese las cantidades y combinarlas")
cheese = int(input("¿Cuántos quesos más necesitas?"))
crackers = int(input("¿Cuántas galletas más requieres?"))

print("Sumando los quesos y galletas adicionales, más los que ya tenías...")
cheese_and_crackers(cheese + amount_of_cheese, crackers + amount_of_crackers)
