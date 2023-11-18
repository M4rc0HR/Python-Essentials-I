# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
 
# del list_1[0]
# del list_2[0]
 
# print(list_3)

# El OUTPUT es:
    # [C]


# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
 
# del list_1[0]
# del list_2
 
# print(list_3)

# El OUTPUT es:
    # [B, C]


# Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
 
# del list_1[0]
# del list_2[:]
 
# print(list_3)

# # El OUTPUT es:
#     # []


# Pregunta 4: ¿Cuál es el resultado del siguiente fragmento de código?


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
 
del list_1[0]
del list_2[0]
 
print(list_3)

# El OUTPUT es:
    # [A, B, C]


#Pregunta 5: Inserta in o not in en lugar de ??? para que el código 
# genere el resultado esperado.

my_list = [1, 2, "in", True, "ABC"]
 
print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False