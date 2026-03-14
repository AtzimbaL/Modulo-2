import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

nombre_astronauta = "Lizbeth"
edad_astronauta = 25
destino = "Saturno"

print(f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}.\n")

combustible = 79
velocidad = 684_925


print(f"Estoy navegando a {velocidad} km/s con {combustible}% de combustible restante hacia {destino}.") 

print("""Fecha: 2026-01-10
      Hoy experimentamos con el cultivo de plantas en microgravedad.
Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!
Fecha: 2026-01-11
Realizamos una caminata espacial para reparar un panel solar. 
Mensaje personal: Flotar en el espacio nunca deja de asombrarme. """)
      
