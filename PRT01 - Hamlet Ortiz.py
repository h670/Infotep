#Hamlet Ortiz 22-1028

"""PRT01 - Operaciones varias
Valor: 5ptos.


Realice un programa que capture 3 números y decir cuál es el mayor de los 3.

Además, 

Si el primero es mayor o igual que el segundo, se realiza lo siguiente:  A + (B x C)
Si el segundo es menor que el tercero, se realiza lo siguiente: C - B
De lo contrario, se realiza lo siguiente: B x C
Al finalizar, mostrar lo siguiente:

Número mayor de los 3.
Operación realizada y su resultado."""

#Bueno en este espacio declare mis variables con mis respectivos input para capturar datos del teclado
num1 = int(input("Ingrese su primer numero: "))
num2 = int(input("Ingrese su segundo numero: "))
num3 = int(input("Ingrese su tercer numero: "))
#en este caso cree mis variables de resultados y concatene los datos y las respuestas que le dara a cada operacion.
Resultado1 = f"Su Primer numero que es {num1} es mayor o igual que el segundo y mayor que el tercero pero con la operacion {num1} + ({num2} * {num3}) es igual a: {num1 +  (num2*num3)}"
Resultado2 = f"Su Segundo numero que es {num2} es mayor, pero con la operacion {num2} * {num3} es igual a: {num2*num3}."
Resultado3 = f"Su Segundo numero que es {num2} solo es menor que el tercero, pero con la operacion {num3} - {num2} es igual a: {num3-num2}."
Resultado4 = f"Su tercer numero que es {num3} es mayor"
#aqui use lo que seria unas ondiciones para que me realice las operaciones necesarias para que el programa que me solicitaron.
if num1 >= num2 and num1 > num3:
    print(Resultado1)
elif num2 > num1 and num2 > num3:
    print(Resultado2)
elif num2 > num1 and num2 < num3:
    print(Resultado3)
elif num3 > num1 and num3 > num2:
    print(Resultado4)
elif num1==num2 and num1==num3 and num2==num3:
    print("Todos son iguales")
    
