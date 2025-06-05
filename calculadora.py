def calculadora():
    print("Bienvenido a la calculadora")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    print("\nSelecciona la operacion: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    operacion = input("Ingrese el numero de la operacion que desea realizar (1,2,3,4): ")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
