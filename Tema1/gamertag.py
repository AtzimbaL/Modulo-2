def cabecera():
    """Muestra la cabecera de la aplicación"""
    # r es para que permita el uso de valores
    titulo = r"""
     _______  _______  _______  _______  _______ _________ _______  _______ 
(  ____ \(  ___  )(       )(  ____ \(  ____ )\__   __/(  ___  )(  ____ \
| (    \/| (   ) || () () || (    \/| (    )|   ) (   | (   ) || (    \/
| |      | (___) || || || || (__    | (____)|   | |   | (___) || |      
| | ____ |  ___  || |(_)| ||  __)   |     __)   | |   |  ___  || | ____ 
| | \_  )| (   ) || |   | || (      | (\ (      | |   | (   ) || | \_  )
| (___) || )   ( || )   ( || (____/\| ) \ \__   | |   | )   ( || (___) |
(_______)|/     \||/     \|(_______/|/   \__/   )_(   |/     \|(_______)
                                                                        
                    ¡Crea tu identidad Gamer!                                                                                                                                                            
    """
    print(titulo)

#cabecera()

def crear_tag_basico(nombre):
    """
    Crea un gamertag basico usando las primeras 4 letras del nombre.
    
    Parametro
    nombre(str): El nombre del usuario
    
    Retorna:
    str Gamertag
    """
    tag = nombre[0:4]
    return tag
    
#tag_basico = crear_tag_basico("Atzimba")
#print(tag_basico)

def crear_tag_invertido(nombre):
    """
    Crea un gamertag invirtiendo el nombre completo
    
    Parametro:
    nombre (str): El nombre del usuario
    
    Retorna:
    str: Gamertag (nombre) invertido
    """
    
    tag = nombre[::-1]
    return tag

#tag_invertido = crear_tag_invertido("Atzimba")
#print(tag_invertido)

def crear_tag_intercalado(nombre, apellido):
    """
    Crea un gamertag combinando letras del nombre y apellido.
    Ejemplo: nombre="Juan", apellido="Perez" → "JPuanerez"
   
    Parámetros:
    nombre (str): El nombre del usuario
    apellido (str): El apellido del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # TU CÓDIGO AQUÍ
    nombre_letra1 = nombre[0]
    apellido_letra1 = apellido[0]
    nombre_resto = nombre[1:]
    apellido_resto = apellido[1:]
    
    print(nombre_letra1, apellido_letra1, nombre_resto,apellido_resto, sep="")
    
crear_tag_intercalado("Atzimba","Morales")

def crear_tag_elite(nombre):
    """
    Crea un gamertag "elite" usando inicio y final del nombre.
    Ejemplo: "Santiago" → "Sago"
    
    Parámetro:
    nombre (str): El nombre del usuario
   
    Retorna:
    None (imprime directamente)
    """
    primerasdos = nombre[:2]
    ultimasdos = nombre[-2:]
    
    print(primerasdos,ultimasdos,sep = "")
    
crear_tag_elite("Atzimba")
    
def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crea un gamertag añadiendo número al final.
    
    Parámetros:
    nombre (str): El nombre del usuario
    numero_favorito (int): Número favorito del usuario
	    
    Retorna:
    None (imprime directamente)
    """
    
    tag1 = nombre[:5]
    
    print(tag1,numero_favorito, sep="")

crear_tag_con_numero("Atzimba",25)

def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
	    
    Parámetro:
    nombre (str): El nombre a analizar
	    
    Retorna:
    None (imprime directamente)
    """
    # pass: para evitar que se ejecute
    longitud = len(nombre)
    primera = nombre[0]
    #ultima = nombre[-1]
    
    print("ESTADÍSTICAS DE TU NOMBRE:")
    print("Nombre completo: ", nombre)
    print(f"Longitud del nombre: {longitud}")
    print(f"Primera letra: {primera}")
    print(f"Última letra:", nombre[-1])
    
mostrar_estadisticas("Atzimba")

# SOLICITAR DATOS
nombre = input("\n Introduce tu nombre: ")
apellido = input("\n Introduce tu apellido: ")
numero = input("\n Introduce tu numero favorito: ")

def generar_todas_las_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags
    
    Parámetros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (str): Numero favorito del usuario
    
    Retorna:
    None: (imprimie directamente)
    """
    
    print("\n==========================================")
    print("Tus opciones de GamerTag:")
    print("\n==========================================")
    
tag_basico = crear_tag_basico(nombre)
print("\n1. TAG BASICO:", tag_basico)
print("\n2. TAG INVERTIDO:", crear_tag_invertido(nombre))
print("\n3. TAG INTERCALADO:", crear_tag_intercalado(nombre, apellido))
print("\n4. TAG ELITE:", crear_tag_intercalado(nombre))
print("\n5. TAG CON NUMERO:", crear_tag_con_numero(nombre,numero))

#---------------------------------
# APLICACION PRINCIPAL
#---------------------------------
# Llamar a la funcion cabecera
cabecera()

# Mostrar estadisticas del nombre
mostrar_estadisticas(nombre)
generar_todas_las_opciones(nombre, apellido)

print("\n ¡Elige tu favorito y conquista el mundo gamer! \n")