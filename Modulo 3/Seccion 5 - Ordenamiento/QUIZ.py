
#COMENTAR       ctrl + k + c
#DESCOMENTAR    ctrl + k + u

# ORDENAMIENTO BURBUJA
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)


# QUIZ

# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?

# lst = ["D", "F", "A", "Z"]
# lst.sort()
 
# print(lst)

# La OUTPUT es:
    # [A, D ,F ,Z]


# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?

# a = 3
# b = 1
# c = 2
 
# lst = [a, c, b]
# lst.sort()
 
# print(lst)

# La OUTPUT es:
    # [1, 2, 3]


# Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?

# a = "A"
# b = "B"
# c = "C"
# d = " "
 
# lst = [a, b, c, d]
# lst.reverse()
 
# print(lst)

# La OUTPUT es:
    # [ , C, B, A]