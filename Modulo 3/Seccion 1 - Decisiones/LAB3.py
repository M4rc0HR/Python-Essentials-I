
año = int(input("Ingrese el año: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if año%4 != 0:
        print("Es un año común")
    elif año%100 != 0:
        print("Es un año bisiesto")
    elif año%400 != 0:
        print("Es un año común")
    else:
        print("Es un año bisiesto")
