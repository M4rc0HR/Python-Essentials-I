ingreso = float(input("Ingrese sus ingresos XD: "))

if ingreso < 85528:
    impuesto = float(ingreso*(0.18) - 556.02)
else:
    impuesto = float(14839.02 + (ingreso-85528)*(0.32))

if(impuesto<=0):
    impuesto = 0
    
print("Su impuesto es de:",round(impuesto,0)," pesos")
