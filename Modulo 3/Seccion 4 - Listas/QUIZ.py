# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?

# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
 
# print(lst)

# La OUTPUT es:
    # [6,2,3,4,5,1]


# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?

# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
 
# for number in lst:
#     add += number
#     lst_2.append(add)
 
# print(lst_2)

# La OUTPUT es:
    # [1,3,6,10,15]


# Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?

# lst = []
# del lst
# print(lst)

# La OUTPUT es:
    # ERROR


# Pregunta 4: ¿Cuál es el resultado del siguiente fragmento de código?

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

# La OUTPUT es:
    # [2,3]
    # 3
