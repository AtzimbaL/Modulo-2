import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

temita = "Python"

def organizar_fiesta(invitados, tema = "tema", lugar = "lugar"):
    print("Preparando una fiesta para ", invitados, " invitados")
    print("Tema de la fiesta: ", tema)
    print("Lugar de la celebración: ", lugar)
    
organizar_fiesta(32)
organizar_fiesta(32, tema = temita)
organizar_fiesta(32, tema = temita, lugar = "Aula de informática")