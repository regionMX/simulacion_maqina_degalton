import random
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    resultados = [0] * (num_niveles + 1)
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            if random.choice([True, False]):
                posicion += 1
        resultados[posicion] += 1
    return resultados

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados, align='center', alpha=0.7)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de una máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Simular la máquina de Galton
resultados = simular_maquina_galton(num_canicas, num_niveles)

# Graficar el histograma
graficar_histograma(resultados)
