"""Hamlet Ortiz
22-1028"""
"""Desarrollar un programa que contenga un menú con las siguientes opciones y se realice lo que se pide para cada una de ellas:

Número par/impar. Capturar un número y determinar si es par o no. Luego, de acuerdo al resultado (True o False), realizar lo siguiente:
Si el número es par, mostrar dicha información y además capturar dos números y determinar si el primero es divisible por el segundo.
Si el número es impar, mostrar dicha información y además capturar dos números mayores a 10, si el primero es mayor que el segundo, realizar una resta; si el segundo es mayor que el primero, realizar una suma; de lo contrario, indicar que ambos números son iguales.
Calcular calificación final. Calcular la calificación final en una asignatura de un estudiante UNPHU. Para ello, se requiere capturar las siguientes informaciones:
Nota Práctica.
Nota PP01.
Nota PP02.
Nota EF.
Luego, efectuar la siguiente fórmula para obtener la nota final: ((PP01 + PP02) / 2) + EF + NP) / 3.

Al finalizar, mostrar la literal obtenida (A, B, C, D o F) y la nota numérica.

Nota: Si el estudiante NO cumple con el mínimo de 70 en la NP y el mínimo de 55 en el EF, obtiene F automáticamente."""
#aqui hago mis print para que vean las opciones del menu
print("1.Numero par/impar.")
print("2.Calcular calificacion final.")
#aqui declaro mis variables
resultado_1 = 0
opcion_1=0
opcion_2 =0 
#cree mis condicionales para que me de las 2 opciones
Opcion_deseada=input("Ingrese la opcion deseada: ")
if Opcion_deseada == "1":
    opcion_1 = int(input("Ingrese un numero: "))
        #AQUI CREE OTRAS CONDICIONES DENTRO DE MIS OTRAS CONDICIONES
    if resultado_1 == opcion_1 % 2: 
        print(f"El numero {opcion_1} es par.")
        primer_num1=int(input("Ingrese el numero 01: "))
        segundo_num1=int(input("Ingrese el numero 02: "))
        #AQUI AGREGO OTRA CONDICION DENTRO DE OTRA CONDICION
        if primer_num1 / segundo_num1:
            print(f"El numero {primer_num1} es divisible entre {segundo_num1}.")
        else: 
            print("No es divisible")
            #EN ESTA CONDICION LE DIGO QUE SI ES DIFERENTE DIGA QUE ES IMPAR
    elif resultado_1 != opcion_1 % 2: 
        print(f"El numero {opcion_1} es impar.")
        #AQUI CAPTURO LOS DATOS
        primer_num2=int(input("Ingrese el numero 01: "))
        segundo_num2=int(input("Ingrese el numero 02: "))
        if primer_num2 and segundo_num2< 10:
            print("Los numeros deben ser mayor a 10. Intente de nuevo.")
        elif primer_num2 > segundo_num2:
            print(f"La resta es {primer_num2} - {segundo_num2} = {primer_num2-segundo_num2}")
        elif segundo_num2 > primer_num2:
            print(f"La suma es {primer_num2} - {segundo_num2} = {primer_num2+segundo_num2}")
        elif primer_num2==segundo_num2: 
            print("Ambos números son iguales.")
            #AQUI ABRO OTRA CONDICION
elif Opcion_deseada == "2":
    a = float(input("Ingrese la nota práctica: "))
    b = float(input("Ingrese la nota del primer parcial: "))
    c = float(input("Ingrese la nota del segundo parcial: "))
    d = float(input("Ingrese la nota del examen final: "))
    resultado_nota = (((b + c) / 2) + d + a) / 3
    if a < 70 or d <55: 
        print("EL estudiante no cumple con lo minimo requerido de NP y/o EF. Literal obtenida: F")
    elif resultado_nota >= 90:
        print("Literal obtenida: A")
        print(resultado_nota)
    elif resultado_nota >= 80 or resultado_nota <90:
        print("Literal obtenida: B")
        print(resultado_nota)
    elif resultado_nota >= 70 or resultado_nota <80:
        print("Literal obtenida: C")
        print(resultado_nota)
    elif resultado_nota >= 60 or resultado_nota <70:
        print("Literal obtenida: D")
        print(resultado_nota)
else:
    print ("Intente Otra vez")    

        
        






