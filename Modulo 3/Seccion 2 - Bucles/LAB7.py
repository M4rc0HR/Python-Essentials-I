#La hipótesis de Collatz

c0 = int(input("Ingrese un número: "))
step = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
        print(round(c0))
        step += 1
    else:
        c0 = 3 * c0 + 1
        print(round(c0))
        step += 1

print("Pasos = ",step)