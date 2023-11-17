blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
bloques_usados = 0
bloques_necesarios = 0
height = 0
while blocks > bloques_necesarios:
    bloques_necesarios += 1
    blocks -= bloques_necesarios
    height += 1
#

print("La altura de la pirámide:", height)

