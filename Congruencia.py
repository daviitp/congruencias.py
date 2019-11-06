##Programa que resuelve congruencias del tipo Ax=B (mod C)
##Autor: David Pazos

##Calcula el MCD entre (A,C).

def euclides(num1,num2):
    if num2 == 0:
        return num1
    return euclides(num2, num1 % num2)

resultados = []

##Calcula todos los resultados de la congruencia, hasta el valor C ingresado (a partir de los cuales se repiten los valores en la solución general).

def congruencia(a,b,c):
    for i in range(0,c):
       if ((a*i - b)%c)== 0 :
          resultados.append(i)

print("De una ecuación en congruencia del tipo Ax=B (mod C): ")        
A = int(input("Escribí A: "))
B = int(input("Escribí B: "))
C = int(input("Escribí C: "))

print("Las soluciones de la ecuación " + str(A) + "x=" + str(B) + " (mod " + str(C)+") " + "son:")
congruencia(A,B,C)
print(resultados)

##La solución general es el primer resultado de la lista de resultados, más el MCD entre (A,C) multiplicado por un k, con k € Z. 

print("La solución general de la ecuación es:")
print("x = " + str(resultados[0]), "+", str(int(C/ euclides(A,C))) + "k")