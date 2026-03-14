# ACTIVIDAD 2 Práctica de operadores: asignación, booleanos y comparación. 

uno = "gato"
dos = "perro"

def comparar_longitud(palabra1, palabra2):
    longitud1 = len(uno)
    longitud2 = len(dos)
    return longitud1 == longitud2

respuesta = comparar_longitud(uno,dos)

print(f"¿Son '{uno}' y '{dos}' dos palabras con la misma longitud? {respuesta}")