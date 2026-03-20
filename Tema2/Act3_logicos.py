palabra_adivinar = "programa"
 
def adivinar_palabra(letra_prueba, palabra_intento):
    """En letra_palabra se define si se encuenta la letra """
    letra_en_palabra = letra_prueba in palabra_adivinar
    adivina1 = palabra_intento == palabra_adivinar
    adivina2 = len(palabra_intento) == len(palabra_adivinar)
    resultado_adivinanza = adivina1 and adivina2
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
    print(f"El jugador gana: {resultado_adivinanza}")
 
adivinar_palabra("k","programa")