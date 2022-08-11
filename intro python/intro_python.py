#Imprimir en consola
print("Hola Python")

#Declaración de variables
# -El tipo de dato es inferido (determinado a través del valor)
miNumero = "Cinco"
# -El tipo de dato puede cambiar
miNumero = 5
#Casting de tipo de dato
print("El valor de miNumero es: "+ str(miNumero))

#Castings más comunes
x = str(3)
y = int(3)
z = float(3)

print("El tipo de dato de x es: "+ str(type(x)))
print("El tipo de dato de x es: "+ str(type(y)))
print("El tipo de dato de x es: "+ str(type(z)))

#condicion
#Hay que considerar la identación
edad = 30
if edad >= 18:
    print("Eres mayor de edad")
    print("Porque tienes 18 o mas")
else:
    print("No eres mayor de edad")
    print("Porque tienes menos de 18")

#Listas
frutas = ["manzana","fresa","mango","guayaba","pera"]
print(frutas[2])

#Ciclo For
#Sólo recorre arreglos

print("Ciclo for")
indice = 0
for fruta in frutas:
    print("Indice: " + str(indice))
    print(fruta)
    indice = indice + 1

for i in range(7):
    print("Número: " + str(i))

#len obtiene el número de elementos de una lista
for i in range(len(frutas)):
    print("Fruta #" + str(i) + ": " + frutas[i])


#Funciones
def mi_funcion():
    print("Estamos dentro de una funcion")

mi_funcion()
#Funcion con parametros
#  -PAramatros con valor predeterminado 
#   (solo se usan si no les mandas un valor)
def mi_funcion_con_parametros(palabra_uno = "Palabra uno", palabra_dos = "Palabra dos"):
    print(palabra_uno + " " + palabra_dos)

mi_funcion_con_parametros("Juan","Perez")
mi_funcion_con_parametros("Ana","García")
mi_funcion_con_parametros()