
# Pregunta 1 ¿Cuál es el resultado del siguiente fragmento de código?
# my_list = [1, 2]
 
# for v in range(2):
#     my_list.insert(-1, my_list[v])
 
# print(my_list)

# El OUTPUT es:
    # [1, 2, 1, 2]


# Pregunta 2 El significado de un argumento posicional está determinado por:
# su posición dentro de la lista de argumentos


# Pregunta 3 ¿Cuáles de los siguientes enunciados son verdaderos respecto al código? (Selecciona dos respuestas)

# nums = [1, 2, 3]
# vals = nums

# nums y vals son diferentes nombres de la misma lista
# nums tiene la misma longitud que vals


# Pregunta 4 Un operador capaz de verificar si dos valores no son iguales se codifica como:
# !=



# Pregunta 5 El siguiente fragmento de código:

# def function_1(a):
#     return None
 
 
# def function_2(a):
#     return function_1(a) * function_1(a)
 
# print(function_2(2))
 
# ERROR


# Pregunta 6 El resultado de la siguiente división:

# print(1 // 2)

# es igual a 0



# Pregunta 7 El siguiente fragmento de código:

# def func(a, b):
#     return b ** a
 
 
# print(func(b=2, 2))

# ERROR


# Pregunta 8 ¿Qué valor se asignará a la variable x?

# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y
# print(x)
# False and True or False and True
# False


# Pregunta 9 ¿Cuáles de los siguientes nombres de variable son ilegales y 
# provocarán una excepción de SyntaxError? (Selecciona dos respuestas)
# in
# for


# Pregunta 10 ¿Cuál es el resultado del siguiente fragmento de código?

# my_list = [x * x for x in range(5)]
 
# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_list))

# [0, 1, 4, 9]


# Pregunta 11 ¿Cuál es el resultado del siguiente fragmento de código?

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
 
# print(x, y, z)

# 1 1 2


# Pregunta 12 ¿Cuál es el resultado del siguiente fragmento de código?

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
 
# print(a, b)

# 0 1


# Pregunta 13 ¿Cuál es el resultado del siguiente fragmento de código?

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))

# 2


# Pregunta 14 Observa el fragmento de código y elige la sentencia verdadera:

# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# nums y vals tienen la misma longitud


# Pregunta 15 ¿Cuál es el resultado del siguiente fragmento de 
# código si el usuario ingresa dos líneas que contienen 3 y 2 respectivamente?

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# 0


# Pregunta 16 ¿Cuál es el resultado del siguiente fragmento de código 
# si el usuario ingresa dos líneas que contienen 3 y 6 respectivamente?

# y = input()
# x = input()
# print(x + y)

# 63



# Pregunta 17 ¿Cuál es el resultado del siguiente fragmento de código?

# print("a", "b", "c", sep="sep")
# asepbsepc
 

# Pregunta 18 ¿Cuál es el resultado del siguiente fragmento de código?

# x = 1 // 5 + 1 / 5
# print(x)

# 0.2


 
# Pregunta 19 Suponiendo que my_tuple es una tupla creada correctamente,
# el hecho de que las tuplas sean inmutables significa que la siguiente instrucción:

# my_tuple[1] = my_tuple[1] + my_tuple[0]

# es ilegal


# Pregunta 20 ¿Cuál es el resultado del siguiente fragmento de código si el usuario
# ingresa dos líneas que contienen 2 y 4 respectivamente?

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# 2.0


# Pregunta 21 ¿Cuál es el resultado del siguiente fragmento de código?

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']
 
# for k in range(len(dct)):
#     v = dct[v]
 
# print(v)

# one



# Pregunta 22 ¿Cuántos elementos contiene la lista lst?

# lst = [i for i in range(-1, -2)]

# cero



# Pregunta 23 ¿Cuáles de las siguientes líneas correctamente invocan la función
# definida a continuación? (Selecciona dos respuestas)

# def fun(a, b, c=0):
#     # Cuerpo de la función.
 
# fun(0, 1, 2) 
# fun(b=0, a=0)




# Pregunta 24 ¿Cuál es el resultado del siguiente fragmento de código?

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)

# print(fun(0, 3))

# 0



# Pregunta 25 ¿Cuántos (*) imprimirá el siguiente fragmento de código en la consola?

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# el fragmento entrará en un bucle infinito, imprimiendo un * por línea



# Pregunta 26 ¿Cuál es el resultado del siguiente fragmento de código?

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# 4


# Pregunta 27 ¿Cuál es el resultado del siguiente fragmento de código?

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")

# ERROR: el código es erróneo (el objeto dict no contiene el método vals())



# Pregunta 28 ¿Cuál es el resultado del siguiente fragmento de código?

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
 
# for x in dct.keys():
#     print(dct[x][1], end="")

# 21



# Pregunta 29 ¿Cuál es el resultado del siguiente fragmento de código?

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# 4



# Pregunta 30 ¿Cuántos (#) imprimirá el siguiente fragmento de código en la consola?

# lst = [[x for x in range(3)] for y in range(3)]
 
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
 
# lst = [[0,1,2],[0,1,2],[0,1,2]]
# ###



# Pregunta 31 ¿Cuál es el comportamiento esperado del siguiente programa si el usuario ingresa 0?

# try:
#     value = input("Ingresa un valor: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada erronea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("¡Buuu!")

# 0.0



# Pregunta 32 ¿Cuál es el comportamiento esperado del siguiente programa?

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
#     print("Mala suerte...")


# ERROR: SyntaxError



# Pregunta 33 ¿Cuál es el comportamiento esperado del siguiente programa?

# foo = (1, 2, 3)
# foo.index(0)

# ERROR: ValueErroR




# Pregunta 34 ¿Cuál de los siguientes fragmentos muestra la forma correcta de manejar múltiples excepciones en una sola cláusula except?

# A:

# try:
#     print("")
# except (TypeError, ValueError, ZeroDivisionError):
#     # Algo de código.
# # B:
# except TypeError, ValueError, ZeroDivisionError:
#     # Algo de código.
# # C:
# except: (TypeError, ValueError, ZeroDivisionError)
#     # Algo de código.
# # D:
# except: TypeError, ValueError, ZeroDivisionError
#     # Algo de código.
# # E:
# except (TypeError, ValueError, ZeroDivisionError)
#     # Algo de código.
# # F:
# except TypeError, ValueError, Zer


# solo A




# Pregunta 35 ¿Qué pasará cuando intentes ejecutar el siguiente código?

# print(¡Hola, Mundo!)

#ERROR: SyntaxError
