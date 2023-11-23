try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except AttributeError:
    print('NO existe un elemento que se necesita!')
except SyntaxError:
    print('Se violan las gramaticas de PYTHON')
except:
    print('Ha sucedido algo extraño, ¡lo siento!')