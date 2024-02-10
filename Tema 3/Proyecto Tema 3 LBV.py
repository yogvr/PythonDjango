# Proyecto del tema
# Vas a crear un programa que, primero le pida al usuario que ingrese un texto. Puede ser un texto cualquier, como un artículo entero, un párrafo, una frase, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección, y a partir de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

texto = input("> Bienvenido. Introduce a continuación un texto de tu elección:\n\t")
tres = input("> Ahora, introduce tres letras de tu elección, separadas por un espacio:\n\t")


# 1.	¿Cuántas veces aparece cada una de las letras que eligió? Para lograr esto, puedes almacenar esas letras en una lista y luego usar algún método propio de string que permita contar cuántas veces aparece un substring dentro del string. Ten en cuenta que al buscar las letras puede haber mayúsculas y minúsculas, y esto afecta al resultado. Hay métodos que pasan letras a minúsculas o mayúsculas.

texto2 = texto.lower()
lista = tres.lower().split()
letra0 = texto2.count(lista[0])
letra1 = texto2.count(lista[1])
letra2 = texto2.count(lista[2])

print(f"\n> Te daré algunas estadísticas.\n\n[1] Frecuencia de las letras. \n> La letra {lista[0]} aparece un total de {letra0} veces en tu texto.\n> La letra {lista[1]} aparece un total de {letra1} veces en tu texto.\n> La letra {lista[2]} aparece un total de {letra2} veces en tu texto.\n\n")


# 2.	Le va a decir al usuario cuántas palabras hay a lo largo de todo el texto. Recuerda que hay un método de string que permite transformarlo en una lista, y que hay funciones que cuentan el largo de una lista.

palabras = texto.split()

print(f"[2] Número de palabras.\n> Tu texto tiene un total de {len(palabras)} palabras.\n\n")


# 3.	Va a informar de cuál es la primera letra del texto y cuál es la última.

print(f"[3] Primera y última.\n> La primera letra de tu texto es {texto[0]}.\n> La última letra de tu texto es {texto[-1]}.\n\n")


#4.	El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.

palabras.reverse()
inverso = " "
inverso = inverso.join(palabras)
print(f"[4] Inversión.\n> Si invertimos el orden de las palabras, tu texto luce así:\n\t{inverso}\n\n")


#5.	El sistema nos va a decir si la palabra “python” se encuentra dentro del texto.

print(f"[5] Python.\n> ¿Se encuentra la palabra \"Python\" dentro de tu texto? Déjame revisar...")

def python():
    if "Python" in palabras:
        numpython= palabras.count("Python")
        print(f"> Sí. En tu texto la palabra \"Python\" figura {numpython} veces.\n\n")
    else:
        print("> Parece que tu texto no incluye esta palabra.\n\n")

python()

print("> No tengo nada más que enseñarte, de momento. Gracias por jugar conmigo.")
