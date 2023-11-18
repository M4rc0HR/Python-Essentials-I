my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
list_aux = my_list[:]
for i in my_list:
    if my_list[i] in list_aux:
        del my_list[i]
        
#
print("La lista con elementos únicos:")
print(my_list)

