from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hola {user_name}, soy el script {script}")
print(f"Me gustaría hacerte algunas preguntas.")
print(f"¿Te agrado, {user_name}? ")
likes = input(prompt)

print(f"¿Donde vives, {user_name}?")
lives = input(prompt)

print(f"¿Qué tipo de computadora tienes?")
computer = input(prompt)

print(f"""
Bien, dijiste que {likes} te agrado.
Vives en {lives}. No estoy seguro de donde esta eso.
Y tienes una computadora {computer}. Bien.
""")

