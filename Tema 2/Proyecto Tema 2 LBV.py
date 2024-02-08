nombre = input("> Hola, ¿cómo te llamas?\n\t")
print(f"> Bienvenido al sistema, {nombre}.\n> Te ayudaremos a calcular tu comisión.")

def ventas():
    ventasinput = input("> Por favor, indica tus ventas mensuales. Introduce un número, sin símbolo de €.\n\t").replace(",", ".")
    ventas = float(ventasinput)
    if type(ventas) != float:
        print("> Por favor, introduce un número válido. Reinicia el programa.")
    if ventas == 0:
        print("> Ya que no has vendido nada este mes, no recibirás ninguna comisión.")
    if ventas < 0:
        print("> Por favor, introduce un número válido. Reinicia el programa.")
    if ventas > 0:
        comision = 0.18*ventas
        print(f"> Tu comisión es de {round(comision,2)}€.\n> Gracias por usar nuestro programa, {nombre}")
    return
        
ventas()