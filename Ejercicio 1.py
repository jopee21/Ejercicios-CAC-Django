### Consigna Ejercicio 1: Escribir una función que calcule el máximo común divisor entre dos números.

def MCD(a, b):
    firstNumber = a
    secondNumber = b
    while b:
        a, b = b, a % b
    
    print('el maximo comun divisor entre',firstNumber,' y ',secondNumber,' es: ', a)
    # return a

#Test de la funcion , pruebo la funcion con 3 pares de numeros, los resultados de
# los mismos son a)4. b)75. c)20.

#Prueba a)
MCD(12,16)
#Prueba b)
MCD(225,300)
#Prueba c)
MCD(380,420)
