# Guillermo De Anda Casas, A01375892
# Ciclos while. Código que contitne las funciones de la misión 7.


def dividir(dividendo, divisor):
    cociente = 0
    divisorAlterado = divisor
    if divisor <= dividendo:
        while divisor <= dividendo:
            cociente += 1
            divisor = divisor + divisorAlterado
            residuo = dividendo - (divisor - divisorAlterado)

    return divisorAlterado, cociente, residuo


def guardarMayor(mayor):
    return mayor


def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    numero = int(input("Teclea un número [-1 para salir]:"))
    numeroAlterado = 0
    if numero == -1:
        print("No hay número mayor")
    else:
        numeroAlterado = int(input("Teclea un número [-1 para salir]:"))
        while numeroAlterado != -1 and numero != -1:

            if numeroAlterado < numero:
                mayor = guardarMayor(numero)
                numeroAlterado = int(input("Teclea un número [-1 para salir]:"))
                numero = numeroAlterado
            elif numeroAlterado >= numero:
                mayor = guardarMayor(numeroAlterado)
                numeroAlterado = int(input("Teclea un número [-1 para salir]:"))
                numero = numeroAlterado
    return mayor


def main():
    print("Misión 07. Ciclos While")
    print("Autor: Guillermo De Anda Casas")
    print("Matrícula: A01375892")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    seleccion = int(input("Teclea tu opción: "))
    while seleccion != 3:
        if seleccion == 1:
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)
            divisorAlterado, cociente, residuo = dividir(dividendo, divisor)
            print("Calculando divisiones")
            print("Dividendo: ",dividendo )
            print("Divisor: ", divisor)
            print(dividendo, "/", divisorAlterado, "=", cociente, ", sobra", residuo)

            print("Misión 07. Ciclos While")
            print("Autor: Guillermo De Anda Casas")
            print("Matrícula: A01375892")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            seleccion = int(input("Teclea tu opción: "))
        elif seleccion == 2:
            print("El mayor es: ", encontrarMayor())
            print("Misión 07. Ciclos While")
            print("Autor: Guillermo De Anda Casas")
            print("Matrícula: A01375892")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            seleccion = int(input("Teclea tu opción: "))
    print(" ")
    print("Gracias por usar este programa, regresa pronto.")


main()