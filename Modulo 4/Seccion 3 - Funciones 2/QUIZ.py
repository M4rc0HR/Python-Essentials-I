# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?

# def hi():
#     return
#     print("¡Hola!")
 
# hi()

# El OUTPUT es:
    # None

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?

# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
 
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))

# El OUTPUT es:
    # True
    # False
    # None

# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código?

# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
 
# print(even_num_lst(11))
 
# El OUTPUT es:
    # 0 2 4 6 8 10


# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código?

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))

# El OUTPUT es:
    # 1, 4, 9 ,16 ,25

