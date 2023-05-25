import math

def calcular_superficie_cuadrado():
    lado = float(input("Ingresa el valor del lado del cuadrado (en cm): "))
    superficie = lado ** 2
    print(f"La superficie del cuadrado es: {superficie} cm²")

def calcular_superficie_rectangulo():
    base = float(input("Ingresa el valor de la base del rectángulo (en cm): "))
    altura = float(input("Ingresa el valor de la altura del rectángulo (en cm): "))
    superficie = base * altura
    print(f"La superficie del rectángulo es: {superficie} cm²")

def calcular_superficie_triangulo():
    base = float(input("Ingresa el valor de la base del triángulo (en cm): "))
    altura = float(input("Ingresa el valor de la altura del triángulo (en cm): "))
    superficie = (base * altura) / 2
    print(f"La superficie del triángulo es: {superficie} cm²")

def calcular_superficie_circulo():
    radio = float(input("Ingresa el valor del radio del círculo (en cm): "))
    superficie = math.pi * (radio ** 2)
    print(f"La superficie del círculo es: {superficie} cm²")

def mostrar_menu():
    print("Seleccione una figura para calcular su superficie:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")

def ejecutar_calculo_superficie():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la figura: ")

        if opcion == "1":
            calcular_superficie_cuadrado()
            break
        elif opcion == "2":
            calcular_superficie_rectangulo()
            break
        elif opcion == "3":
            calcular_superficie_triangulo()
            break
        elif opcion == "4":
            calcular_superficie_circulo()
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

ejecutar_calculo_superficie()