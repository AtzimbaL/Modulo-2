# ========================================== 

# CALCULADORA DE FITNESS Y SALUD PERSONAL 

# ========================================== 
nombre = "Atzimba"
peso = 65
altura = 1.64
alturacm = altura * 100
edad = 25
es_hombre = False

def calcular_imc(peso_kg, altura_m): 

    """ 
    Calcula el Índice de Masa Corporal (IMC). 

    Fórmula: IMC = peso / (altura^2) 

    Parámetros: 
    peso_kg (float): Peso en kilogramos 
    altura_m (float): Altura en metros 

    Retorna: 
    float: El IMC calculado 
    """ 
    
    imc = peso_kg / (altura_m ** 2) 
    return imc 

imc = calcular_imc(peso, altura)

def es_peso_saludable(imc): 

    """ 
    Determina si el IMC está en rango saludable (18.5 - 24.9).

    Parámetro: 
    imc (float): Índice de Masa Corporal 

    Retorna: 
    bool: True si está en rango saludable, False si no 
    """ 
    
    # Operadores de comparación y lógicos 
    return imc >= 18.5 and imc <= 24.9 

def tiene_sobrepeso(imc): 

    """ 
    Determina si hay sobrepeso (IMC >= 25). 

    """ 
    # TU CÓDIGO AQUÍ
    return imc >= 25

def tiene_bajo_peso(imc): 

    """ 

    Determina si hay bajo peso (IMC < 18.5). 

    """ 

    # TU CÓDIGO AQUÍ
    return imc < 18.5 

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre): 

    """ 
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict. 

    Parámetros: 
    peso_kg (float): Peso en kg 
    altura_cm (float): Altura en cm 
    edad (int): Edad en años 
    es_hombre (bool): True si es hombre, False si es mujer      

    Retorna: 
    float: Calorías diarias recomendadas 

    """ 

    # Operadores aritméticos y booleanos 

    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad) 
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    
    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad) 
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)

    # Usa el hecho de que True=1 y False=0 

    # TU CÓDIGO AQUÍ 
    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer 

calcular_calorias_diarias(peso, alturacm , edad, es_hombre)

def calcular_agua_diaria(peso_kg): 

    """ 
    Calcula litros de agua recomendados al día (35ml por kg de peso). 

    """ 

    # TU CÓDIGO AQUÍ 
    ml_agua = peso_kg * 35
    litros_agua = ml_agua / 1000 
    return litros_agua 

calcular_agua_diaria(peso)

def calcular_ritmo_cardiaco_maximo(edad): 

    """ 
    Calcula el ritmo cardíaco máximo (220 - edad). 
    """ 

    # TU CÓDIGO AQUÍ 
    return 220 - edad

calcular_ritmo_cardiaco_maximo(edad)

print(f"Te ayudaremos a calcular tu IMC {nombre}")
print(f"Tu IMC es: {imc}")
print(f"¿Tu peso es saludable? {es_peso_saludable(imc)}")
print(f"¿Tienes sobrepeso? {tiene_sobrepeso(imc)}")
print(f"¿Tienes bajo peso? {tiene_bajo_peso(imc)}")
print(f"Tienes {calcular_calorias_diarias(peso, alturacm , edad, es_hombre)} calorias diarias")
print(f"Deberias tomar {calcular_agua_diaria(peso)} litros de agua")
print(f"Tu ritmo cardiaco es de: {calcular_ritmo_cardiaco_maximo(edad)} ppm")