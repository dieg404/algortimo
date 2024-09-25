import random

#Diccionario que almacena informacion de tareas
process = {
    "Tarea": [],
    "Rafaga de CPU": [],
    "Tiempo de llegada": []
}

#Funcion que da aleaotriamenten una palabra de una lista
def word(message):
    return random.choice(message)

#Funcion para generar un número aleatorio desde 0 hasta 20
def random_one():
    return random.randrange(1, 20)
    
#Funcion para generar un número aleatorio desde 0 hasta 10
def random_two():
    return random.randrange(1, 10)


#Lista de procesos
processes = [
    "excel",
    "paint",
    "photoshop",
    "word",
    "notepad",
    "explorer",
    "chrome",
    "firefox",
    "powershell",
    "cmd",
    "calculadora",
    "brave",
    "configuracion",
    "one drive",
    "camara",
    "visual studio code",
    "valorant",
    "acrobat reader",
    "fotos"
]

#Inicio de codigo
x = random_one()
for i in range(x):
    k = random_two()

    process["Tarea"].append(word(processes))
    process["Rafaga de CPU"].append(k)
    process["Tiempo de llegada"].append(k)

print(x)
print(process)

#Version 1
#Se define estructura de diccionario donde se almacenara los datos de las tareas
#Se define una funcion que escogera una palabra de una lista ya definida
#Se define una funcion que genera un número aleatorio entre 1 y 20
#Se define una funcion que se genera un número aleatorio entre 0 y 10
#Se define una lista donde almacena 20 procesos
#Se inicia el codigo