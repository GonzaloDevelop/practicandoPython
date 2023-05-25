#encoding:UTF-8
import random

while True: 
    aleatorio = random.randrange(0, 5)
    elijePc = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Salir del Programa")
    opcion = int(input("¿Qué eliges?: "))
    
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
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue
        
    print("Tu eliges: ", eligeUsuario)   
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
    print("PC eligio: ", eligePc)
    print("...")

    if eligePc == "piedra" and eligeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
    elif eligePc == "papel" and eligeUsuario == "tijera":
        print("Ganaste, tijera corta papel")
    elif eligePc == "tijera" and eligeUsuario == "piedra":
        print("Ganaste, piedra pisa tijera")
    if eligePc == "spock" and eligeUsuario == "piedra":
        print("Perdiste, spock vaporiza piedra")
    if eligePc == "lagarto" and eligeUsuario == "spock":
        print("Perdiste, lagarto envenena spock")
    if eligePc == "lagarto" and eligeUsuario == "papel":
        print("Perdiste, lagarto devora papel")
    if eligePc == "piedra" and eligeUsuario == "lagarto":
        print("Perdiste, piedra aplasta lagarto")
    if eligePc == "spock" and eligeUsuario == "tijera":
        print("Perdiste, spock rompe tijera")
    if eligePc == "tijera" and eligeUsuario == "lagarto":
        print("Perdiste, tijera decapita lagarto")
    if eligePc == "papel" and eligeUsuario == "spock":
        print("Perdiste, papel desautoriza spock")
    
    
    if eligeUsuario == "piedra" and eligePc == "papel":
        print("Perdiste, papel envuelve piedra")
    elif eligeUsuario == "papel" and eligePc == "tijera":
        print("Perdiste, tijera corta papel")
    elif eligeUsuario == "tijera" and eligePc == "piedra":
        print("Perdiste, piedra pisa tijera")
    if eligeUsuario == "spock" and eligePc == "piedra":
        print("Ganaste, spock vaporiza piedra")
    if eligeUsuario == "lagarto" and eligePc == "spock":
        print("Ganaste, lagarto envenena spock")
    if eligeUsuario == "lagarto" and eligePc == "papel":
        print("Ganaste, lagarto devora papel")
    if eligeUsuario == "piedra" and eligePc == "lagarto":
        print("Ganaste, piedra aplasta lagarto")
    if eligeUsuario == "spock" and eligePc == "tijera":
        print("Ganaste, spock rompe tijera")
    if eligeUsuario == "tijera" and eligePc == "lagarto":
        print("Ganaste, tijera decapita lagarto")
    if eligeUsuario == "papel" and eligePc == "spock":
        print("Ganaste, papel desautoriza spock")

    elif eligePc == eligeUsuario:
        print("Empate")

    again = input("Jugamos de nuevo? Si/No: ")
    if 'si' in again:
        continue
    elif 'no' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")