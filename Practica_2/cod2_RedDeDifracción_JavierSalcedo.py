'''
Práctica de Laboratorio #2
Red de Difracción
Javier A. Salcedo Castañeda
Departamento de Física, Facultad de Ciencias, Universidad de Los Andes (ULA)
'''

import numpy as np
import matplotlib.pyplot as plt

########## Caracterización de la red de difracción ##########

# Calibración de la red de difracción

## Ajuste de la red de difracción para que esté perpendicular al haz de luz incidente.

ref = 79+(0.04/0.60)
ang_1I = np.abs(57+(0.57/0.60)-ref)
ang_1D = np.abs(58+(0.01/0.60)-ref)

promedio_1 = (ang_1D+ang_1I)/2

ang1I = np.abs(100+(0.02/0.60)-ref)
ang1D = np.abs(100+(0.06/0.60)-ref)

promedio1 = (ang1D+ang1I)/2

print('Ángulos de calibración m=1')
print('Izq',promedio1,'Der', promedio_1)
print('Izq',np.deg2rad(promedio1),'Der', np.deg2rad(promedio_1))

## Calcular el número de líneas iluminadas N.

lambda_I = 589.0
lambda_D = 589.6 
N = ((589.6+589.0)/2)/(589.6-589.0)
print('Número de líneas iluminadas', N)

## Calcular la distancia entre líneas d.

m = 1
d = m*589.3/(982*np.sin(np.deg2rad(promedio1)))
print('Distancia entre líneas', d*10**(-3))

## Calcular la densidad de líneas sigma.

sigma = 1/(d*10**(-3))
print('Densidad de líneas', sigma)

## Calcular el poder de dispersión D.

D = m/(d*np.sin(promedio1))
print('Poder de dispersión', D)

## Calcular el poder de resolución R.
""" En este caso como m=1, el poder de resolución es igual al poder de dispersión. """

print('Resolución', N)


########## Curva de calibración ##########

radianes = np.array([0.268, 0.285, 0.320, 0.355, 0.376, 0.377, 0.394, 0.398, 0.406])
longitud_onda_experimental = np.array([443.60,470.30,526.55,581.23,613.98,616.69,642.86,649.15, 661.70])*10

a, b = np.polyfit(radianes, longitud_onda_experimental, 1)
print(f'Pendiente (a): {a:.2f}, Intersección (b): {b:.2f}')
#longitud_onda_experimental = (a * radianes + b) * 100

plt.scatter(radianes, longitud_onda_experimental, color='blue', label='Datos experimentales')
plt.plot(radianes, longitud_onda_experimental, color='red', linestyle='--', label=f'Ajuste lineal: λ = {a:.2f}θ + {b:.2f}')
plt.xlabel('Ángulo (rad)')
plt.ylabel('Longitud de onda (Å)')
plt.title('Curva de calibración de la red de difracción (Mercurio)')
plt.xticks(np.arange(0.25, 0.45, 0.02))
plt.legend()
plt.show()

########## Fuentes desconocidas ##########

# Función para graficar y comparar con diferentes fuentes de luz con espectros de referencia
def graficar_fuente(radianes, a, b, titulo, longitudes_referencia=np.array([]), color_referencia='white'):
    lambda_curva = (a * radianes + b)
    print('longitud de onda')
    print(lambda_curva)

    plt.scatter(radianes, lambda_curva, color='blue', label='Datos experimentales')
    plt.plot(radianes, lambda_curva, color='red', linestyle='--', label=f'Ajuste lineal: λ = {a:.2f}θ + {b:.2f}')
    if len(longitudes_referencia) > 0:
        radianes_tabulados = (((np.array(longitudes_referencia) - b+30) / a))
        plt.scatter(radianes_tabulados, longitudes_referencia, color=color_referencia, marker='x', label='Datos tabulados')
        plt.plot(radianes_tabulados, longitudes_referencia, color=color_referencia, linestyle='--', label='Datos tabulados')
    else:
        None

    plt.xlabel('Ángulo (rad)')
    plt.ylabel('Longitud de onda (Å)')
    plt.title(titulo)
    plt.xticks(np.arange(0.25, 0.45, 0.02))
    plt.legend()
    plt.show()

## Fuente desconocida 5C

fuente_5C = np.array([0.252,0.259,0.278,0.291,0.305,0.311,0.313,0.367,0.419])
graficar_fuente(fuente_5C, a, b, 'Curva de fuente desconocida 5C')

## Fuente desconocida 6F

fuente_6F = np.array([0.250,0.300,0.412])
graficar_fuente(fuente_6F, a, b, 'Curva de fuente desconocida 6F')

## Fuente desconocida 5B

fuente_5B = np.array([0.272,0.276,0.309,0.304,0.311,0.312,0.366,0.419])
graficar_fuente(fuente_5B, a, b, 'Curva de fuente desconocida 5B')

##### Comparación de elementos para determinar gas de la fuente desconocida #####

## Elementos y sus longitudes de onda de emisión (tabulados) para comparar con las fuentes desconocidas
elementos = {
    "hidrógeno": [4200, 4400, 4900, 6700],
    "deuterio": [4200, 4400, 4900, 6700],
    "helio": [4000, 4500, 4550, 4800, 5000, 5100, 5850, 6500, 6800, 7200],
    "nitrógeno": [4000, 4050, 4100, 4150, 4200, 4250, 4400, 4450, 5000, 5050, 5200, 5300, 5400, 5500, 5600, 5800, 5850, 5900, 6000, 6150, 6200, 6250, 6300, 6350, 6400, 6450, 6500, 6600, 6700, 6750, 6800, 6850],
    "oxígeno": [4400, 4900, 5250, 5400, 5500, 5650, 6150, 6250, 6600, 6650],
    "agua": [4300, 4400, 4900, 5200, 5400, 5500, 5600, 6050, 6100, 6650],
    "dióxido_de_carbono": [4150, 4250, 4450, 4550, 4900, 5100, 5200, 5300, 5400, 5500, 5600, 5650, 5900, 6100, 6200, 6250, 6300, 6400, 6500, 6600, 6700, 6800, 7100],
    "ácido_carbónico": [4150, 4250, 4450, 4550, 4900, 5100, 5200, 5300, 5400, 5500, 5600, 5650, 5900, 6100, 6200, 6250, 6300, 6400, 6500, 6600, 6700, 6800, 7100],
    "neón": [4750, 4900, 5100, 5250, 5600, 5700, 5800, 5900, 6000, 6050, 6100, 6150, 6200],
    "argón": [4200, 4400, 4650, 4950, 5250, 5500, 5600, 5700, 5950, 6250, 6400, 6500, 6700, 6800, 7100],
    "criptón": [4300, 4400, 4500, 4550, 4900, 5600, 5650, 5700, 5900, 6100, 6300, 6500, 6650],
    "xenón": [4700, 4850, 5000, 6250, 6400],
    "mercurio": [4500, 4600, 5000, 5050, 5600, 5900, 6100, 6250, 6600, 6800],
    "cloro": [4450, 4550, 4850, 5100, 5200, 5400, 5450, 5700, 5900, 6000, 6250, 6350, 6550, 6650],
    "bromo": [4200, 4250, 4500, 4750, 4800],
}

##### Fuentes desconocidas y espectro de gas que se cree que contienen #####

# Fuente desconocida 5C
graficar_fuente(fuente_5C, a, b, 'Curva de fuente desconocida 5C (Helio)', elementos['helio'], 'orange')

# Fuente desconocida 6F
graficar_fuente(fuente_6F, a, b, 'Curva de fuente desconocida 6F (Hidrógeno)', elementos['hidrógeno'], 'orange')
graficar_fuente(fuente_6F, a, b, 'Curva de fuente desconocida 6F (Deuterio)', elementos['deuterio'], 'orange')

# Fuente desconocida 5B
graficar_fuente(fuente_5B, a, b, 'Curva de fuente desconocida 5B (Criptón)', elementos['criptón'], 'orange')
graficar_fuente(fuente_5B, a, b, 'Curva de fuente desconocida 5B (Mercurio)', elementos['mercurio'], 'orange')



