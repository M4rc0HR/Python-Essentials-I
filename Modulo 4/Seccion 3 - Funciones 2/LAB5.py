def liters_100km_to_miles_gallon(liters):
    val =(100000 * 3.785411784)/ (liters * 1609.344)
    return val

def miles_gallon_to_liters_100km(miles):
    val = (3.785411784*100000)/(miles * 1609.344)
    return val

    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


