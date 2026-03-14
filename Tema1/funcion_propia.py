def contar_caracteres(arg1):
    longitud = len(arg1)
    print(f"La frase", arg1, f"tiene: {longitud} caracteres")
    
#frase = "Aprender Python es divertido"
contar_caracteres(arg1="Aprender Python es divertido")

def convertir_numero(arg2):
    entero = int(arg2)
    cadena = str(arg2)
    flotante = float(arg2)
    
    tipo_int = type(entero)
    tipo_str = type(cadena)
    tipo_float = type(flotante)
    
    print(f"Entero: {entero}, Tipo: {tipo_int}")
    print(f"Cadena: {cadena}, Tipo: {tipo_str}")
    print(f"Flotante: {flotante}, Tipo: {tipo_float}")
    
num_int = 23
convertir_numero(arg2=num_int)