#encoding:UTF-8
import random
import sys
import pickle

def get_int():
    userdata = input("Ingrese un número, o 'exit' para salir del programa ")
    if userdata == 'exit':
        print("¡Nos vemos!")
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Necesito un número para continuar: ")
        return get_int()
puntajeUsuario = 0
puntajePc = 0
puntajeTotal = 0

def porcentaje():
    if puntajeTotal > 0:
        x = (puntajeUsuario / puntajeTotal) * 100
        return x
    elif puntajeTotal == 0:
        x = 0
        return x

try:
    with open("puntajes.dat", "rb") as file:
        puntajes = pickle.load(file)
        puntajeUsuario = puntajes["usuario"]
        puntajePc = puntajes["pc"]
        puntajeTotal = puntajes["total"]
        print("Puntajes cargados exitosamente.")
except FileNotFoundError:
    print("No se encontró el archivo de puntajes. Se crearán nuevos puntajes.")

while True:
    aleatorio = random.randrange(0, 5)
    elijePc = ""
    again = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Mostrar Puntajes")
    print("7) Salir del Programa")
    opcion = get_int()

    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    elif opcion == 4:
        eligeUsuario = "lagarto"
    elif opcion == 5:
        eligeUsuario = "spock"
    elif opcion == 6:
        print("Puntajes:")
        print("Usuario:", puntajeUsuario)
        print("PC:", puntajePc)
        print("Porcentaje de victorias:", porcentaje(), "%")
        continue
    elif opcion == 7:
        print("¡Nos vemos!")
        break
    else:
        print("Opción inválida")
        continue

    print("Tu eliges:", eligeUsuario)
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    elif aleatorio == 3:
        eligePc = "lagarto"
    elif aleatorio == 4:
        eligePc = "spock"
    print("PC eligió:", eligePc)
    print("...")

    ganaUsuario = 0
    ganaPc = 0

    if eligePc == "piedra" and eligeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
        ganaUsuario = 1
    elif eligePc == "papel" and eligeUsuario == "tijera":
        print("Ganaste, tijera corta papel")
        ganaUsuario = 1
    elif eligePc == "tijera" and eligeUsuario == "piedra":
        print("Ganaste, piedra pisa tijera")
        ganaUsuario = 1
    if eligePc == "spock" and eligeUsuario == "piedra":
        print("Perdiste, spock vaporiza piedra")
        ganaPc = 1
    if eligePc == "lagarto" and eligeUsuario == "spock":
        print("Perdiste, lagarto envenena spock")
        ganaPc = 1
    if eligePc == "lagarto" and eligeUsuario == "papel":
        print("Perdiste, lagarto devora papel")
        ganaPc = 1
    if eligePc == "piedra" and eligeUsuario == "lagarto":
        print("Perdiste, piedra aplasta lagarto")
        ganaPc = 1
    if eligePc == "spock" and eligeUsuario == "tijera":
        print("Perdiste, spock rompe tijera")
        ganaPc = 1
    if eligePc == "tijera" and eligeUsuario == "lagarto":
        print("Perdiste, tijera decapita lagarto")
        ganaPc = 1
    if eligePc == "papel" and eligeUsuario == "spock":
        print("Perdiste, papel desautoriza spock")
        ganaPc = 1
    if eligeUsuario == "piedra" and eligePc == "papel":
        print("Perdiste, papel envuelve piedra")
        ganaPc = 1
    elif eligeUsuario == "papel" and eligePc == "tijera":
        print("Perdiste, tijera corta papel")
        ganaPc = 1
    elif eligeUsuario == "tijera" and eligePc == "piedra":
        print("Perdiste, piedra pisa tijera")
        ganaPc = 1
    if eligeUsuario == "spock" and eligePc == "piedra":
        print("Ganaste, spock vaporiza piedra")
        ganaUsuario = 1
    if eligeUsuario == "lagarto" and eligePc == "spock":
        print("Ganaste, lagarto envenena spock")
        ganaUsuario = 1
    if eligeUsuario == "lagarto" and eligePc == "papel":
        print("Ganaste, lagarto devora papel")
        ganaUsuario = 1
    if eligeUsuario == "piedra" and eligePc == "lagarto":
        print("Ganaste, piedra aplasta lagarto")
        ganaUsuario = 1
    if eligeUsuario == "spock" and eligePc == "tijera":
        print("Ganaste, spock rompe tijera")
        ganaUsuario = 1
    if eligeUsuario == "tijera" and eligePc == "lagarto":
        print("Ganaste, tijera decapita lagarto")
        ganaUsuario = 1
    if eligeUsuario == "papel" and eligePc == "spock":
        print("Ganaste, papel desautoriza spock")
        ganaUsuario = 1

    if eligeUsuario == eligePc:
        print("Empate!")

    if ganaUsuario == 1:
        puntajeUsuario += 1
        puntajeTotal += 1
    elif ganaPc == 1:
        puntajePc += 1
        puntajeTotal += 1

    print("Puntajes:")
    print("Usuario:", puntajeUsuario)
    print("PC:", puntajePc)
    print("Porcentaje de victorias:", porcentaje(), "%")

    puntajes = {
        "usuario": puntajeUsuario,
        "pc": puntajePc,
        "total": puntajeTotal
    }
    with open("puntajes.dat", "wb") as file:
        pickle.dump(puntajes, file)
        print("Puntajes guardados exitosamente.")

    print("¿Jugamos de nuevo? Si/No: ")
    again = input()
    if again == "no":
        print("¡Nos vemos!")
        sys.exit()