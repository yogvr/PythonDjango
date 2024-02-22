## EJERCICIO 1
#Crea una clase llamada Personaje y a continuación, crea un objeto a partir de ella, por ejemplo: hector_barbossa 

class Personaje:
    pass
hector_barbossa = Personaje()



## EJERCICIO 2
#2. Crea una clase llamada  Clase, y tres instancias a partir de ella: mago, paladin y arquero. 

class Clase:
    pass

mago = Clase()
paladin = Clase()
arquero = Clase()



## EJERCICIO 3
#3. Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: netflix, hbo_max, amazon_prime_video. 

class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()



## EJERCICIO 4
#4. Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos. Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        pass

casa_blanca = Casa("blanco", 4)



## EJERCICIO 5
#5. Crea una clase llamada Cubo, y asígnale el atributo de clase “caras = 6”, y el atributo de instancia “color”. Crea una instancia cubo_rojo, de dicho color. 

class Cubo:
    caras = 6
    def __init__(self,color)
        self.color = color
        pass

cubo_rojo = Cubo("rojo")



## EJERCICIO 6
#6. Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase, “real = False”. Crea una instancia llamada inosuke_hashibira con los siguientes atributos de instancia: a) especie = “¿Humano?” b) magico = False c) edad = 15 

class Personaje:
    real = False
    def __init__(self,especie,magico,edad)
        self.especie = especie
        self.magico = magico
        self.edad = edad
        pass

inosuke_hasibira = Personaje("¿Humano?", False, 15)



## EJERCICIO 7
#7. Crea una clase Perro. Dicho perro debe poder ladrar. Crea el método  ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "¡Guau!". 

class Perro():
    def __init__(self, color):
        self.color = color
        pass

    def ladrar(self):
        return print("¡Guau!")

caniche = Perro("blanco")
caniche.ladrar()



## EJERCICIO 8
#8. Crea  una  clase  llamada  Mortifago,  y  crea  un  método  llamado maldicion_imperdonable(),  que  deberá  imprimir  "¡Avada  Kedavra!".  Crea  una instancia de Mago en el objeto bellatrix, y haz que lance un hechizo. 

class Mortifago:
    def maldicion_imperdonable(self):
        return print("¡Avada Kedavra!")

class Mago:
    def hechizo(self):
        return print("El mago lanza un hechizo.")

mortifago = Mortifago()
bellatrix = Mago()

mortifago.maldicion_imperdonable()
bellatrix.hechizo()



## EJERCICIO 9
#9. Crea  una  instancia  de  la  clase  Alarma,  que  tenga  un  método  llamado aplazar(cantidad_minutos). El método debe imprimir en pantalla el mensaje “La alarma ha sido atrasada {cantidad_minutos} minutos”. 

class Alarma:
    def aplazar(self,cantidad_minutos):
        self.cantidad_minutos = cantidad_minutos
        return print (f"La alarma ha sido aplazada {cantidad_minutos} minutos")

reloj = Alarma()
reloj.aplazar(4)



## EJERCICIO 10
#10. Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar".

class Mascota:
    @staticmethod
    def respirar():
        return print("Inhalar... Exhalar")



## EJERCICIO 11
#11. Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False. 
    
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        vivo = True
        return



## EJERCICIO 12
#12. Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flecha que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas. 

class Personaje:
    def __init__(self,cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        return print(self.cantidad_flechas)

    

## EJERCICIO 13
#13. Crea  una  clase  llamada  Persona,  que  tenga  los  siguientes  atributos  de  instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos. 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        pass

class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    pass



## EJERCICIO 14   
#14. Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos. 

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        pass

class Perro(Mascota):
     def __init__(self, edad, nombre, cantidad_patas):
         super().__init__(edad, nombre, cantidad_patas)
         pass


## EJERCICIO 15
#15. Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo. 

class Vehiculo:
    def acelerar(self):
        print("Ruuuuuu")
        return

    def frenar(self):
        print("Riiiiiii")
        return

class Automovil(Vehiculo):
    pass

ferrari = Automovil()

ferrari.frenar()


#16. Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a  esta  clase  heredar  correctamente  de  Padre  y  Madre.  Completa  el  código suministrado a continuación para lograrlo.

class Padre():
    def trabajar(self):
        print ("Trabajando en el Hospital")
    
    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass


#17. "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías, pero no tiene mamas." (National Geographic).Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos: a) poner_huevos() b) tiene_pico = True c) vertebrado = True d) venenoso = True e) nadar() f) caminar() g) amamantar()

class Vertebrado:
    vertebrado = True

class Pez(Vertebrado):
    def nadar(self):
        pass
    def poner_huevos(self):
        pass

class Reptil(Vertebrado):
    venenoso = True
    def poner_huevos(self):
        pass

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        pass

class Mamifero(Vertebrado):
    def amamantar(self):
        pass
    def caminar(self):
        pass

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass


#EJERCICIO 18
##18. Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobrescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre". Asegúrate de utilizar return seguido de una cadena de texto.

class Padre:
    def __init__(self,nombre,color_favorito):
        self.nombre = nombre
        self.color_favorito = color_favorito
    
    def roncar(self):
        return print("Brrrr fiuuu")
    
    def hobby(self):
        return print("Cocino en mi tiempo libre")
    
class Hijo(Padre):
    def __init__(self,nombre,color_favorito):
        super().__init__(nombre,color_favorito)
    
    def hobby(self):
        return print("Juego videojuegos en mi tiempo libre")



# EJERCICIO 19
##19. La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de ítems o caracteres que lo componen. Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

def iterador(*args):
    for i in args:
        print(len(i))
    
string = "abcdefg"
lista = [990, 44, -20]
tupla = ("blanco", "negro")

iterador(string,lista,tupla)



# EJERCICIO 20
##20. Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos. Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrerse en dicho orden.

class Arquero:
    def atacar(self):
        return print("El arquero lanza una flecha.")

class Mago:
    def atacar(self):
        return print("El mago lanza un hechizo.")
    
class Samurai:
    def atacar(self):
        return print("El samurai usa su katana.")
    
arquero1 = Arquero()
mago1 = Mago()
samurai1 = Samurai()

personajes = [arquero1, mago1, samurai1]

iterador = [pj.atacar() for pj in personajes]



# EJERCICIO 21
##21. Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos. Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

class Hechicero:
    def personaje_defender(self):
        return print ("El hechicero crea un campo de fuerza.")

class Druida:
    def personaje_defender(self):
        return print ("El druida crea un escudo de raíces.")
    
class Luchador:
    def personaje_defender(self):
        return print ("El luchador se defiende con su escudo.")

hechicero1 = Hechicero()
druida1 = Druida()
luchador1 = Luchador()

def personaje_defender(personaje):
    return personaje.personaje_defender()


    
# EJERCICIO 22
## 22. Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva “{titulo}”, de ‘{autor}' (atención: el título debe estar encerrado entre comillas dobles)

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    
    def __str__(self):
        return f"\"{self.titulo}\" de \"{self.autor}\""
    


# EJERCICIO 23
##23. Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    
    def __len__(self):
        return int(cantidad_paginas)



# EJERCICIO 24
## 24. Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.

class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        return "Libro eliminado"