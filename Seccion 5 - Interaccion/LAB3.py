hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.

mins = mins + dura
hour = hour + mins // 60
mins %= 60
hour %= 24
print(hour, ":", mins, sep='')
