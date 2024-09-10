def restar(x, y):
    return x - y

def multiplicacion(x, y): 
    return x * y

def divisio(x, y):
    if y == 0:
        return "No se puede dividir por 0"
    else:
        return x / y

respuesta=multiplicacion(2,3)
print(respuesta)

resultado=restar(8,2)
print("CAMBIO" + str(resultado))