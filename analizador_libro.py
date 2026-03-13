import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

libro1 = "Matematicas"
libro2 = "Ciencias Naturales"
libro3 = "Programación con Python"

long1 = len(libro1)
long2 = len(libro2)
long3 = len(libro3)

print(f"La longitud del título del libro 1 es: {long1}")
print(f"La longitud del título del libro 2 es: {long2}")
print(f"La longitud del título del libro 3 es: {long3}")