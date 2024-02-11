# Ejercicios – Tema 1
#1.	Crea un código que imprima en pantalla la expresión Me encanta aprender Python
print("Me encanta aprender Python")

#2.	Imprime por pantalla la expresión Estudiar “Python” puede ser muy divertido
print("Estudiar \"Python\" puede ser muy divertido")

#3.	Imprime por pantalla el número 555, pero que sea resultado de una operación matemática
print(int((4**0.5+3)*100+55))

#4.	Imprime en pantalla la siguiente expresión (pero usando print una sola vez):
"""
a)	Línea 1
b)	Línea 2
c)	Línea 3
"""
print("a)\tLínea 1\n""b)\tLínea 2\n""c)\tLínea 3")

#5.	Imprime en pantalla la siguiente expresión.
"""
a)	A B 		C
b)	D E 		F
c)	G H 		I
"""
print("a)\tA B \t\tC\n""b)\tD E \t\tF\n""c)\tG H \t\tI")


#6.	Imprime en pantalla la siguiente expresión:
"""
a)	Barra Normal: /
b)	Barra Invertida: \
"""
print("a)\tBarra Normal: /\n""b)\tBarra Inversa: \\")

#7.	Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta: ¿Qué estás estudiando? El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

print("Estás estudiando " + input("¿Qué estás estudiando?\n"))

#8.	Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta: ¿En qué país vives? El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).
print("Vives en " + input("¿En qué país vives?\n"))

#9.	Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:
"""
a)	Escribe tu nombre:
b)	Escribe tu apellido:  
"""
#El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.
print(input("a)\tEscribe tu nombre:\n ") + " " + input("b)\tEscribe tu primer apellido:\n "))

#Proyecto del tema 
#Vas a crear un código que le pida al usuario que responda dos preguntas que requieran una sola palabra cada una, y que luego le muestre en pantalla esas palabras combinadas para formar una marca.

print("Tu marca es:\n", input("¿Cuál es tu animal favorito?\n"), input("¿De qué color es tu cepillo de dientes?\n"))