import numpy as np
import matplotlib.pyplot as plt


# Ley de Malus

intensity = np.array([8.8, 8.4, 7.6, 6.4, 5.2, 3.6, 2, 0.8, 0.2, 0, 0.2, 0.8, 2.2, 3.6, 5.2, 6.6, 7.8, 8.4, 8.8, 8.4, 7.8, 6.6, 5, 3.4, 2, 0.8, 0.2, 0, 0.2, 0.8, 2, 3.6, 5.2, 6.4, 7.8, 8.6, 8.8])
angle = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360])
intensidad = 8.8 * np.cos(np.radians(angle))**2

plt.plot(angle, intensidad, 'r-')
plt.plot(angle, intensity, 'o-')
plt.title('Ley de Malus')
plt.xlabel('Ángulo (grados)')
plt.ylabel('Intensidad (arbitraria)')
plt.grid()

plt.legend(['Datos experimentales', 'Ley de Malus'], loc='upper left')

plt.ylim(-0.5, 11)
plt.show()


#Polarización por Birrefringencia con un Retardador

angulos = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])

intensidad_angulo_0 = np.array([8, 7.8, 7.2, 6.2, 4.8, 3.4, 2.2, 1, 0.2, 0, 0.2, 0.8, 1.6, 3, 4.4, 5.6, 6.8, 7.4, 8])
intensidad_angulo_10 = np.array([7.4, 7.6, 7.6, 7, 6.2, 4.8, 3.6, 2.4, 1.2, 0.4, 0.2, 0.4, 0.8, 1.8, 3, 4.2, 5.4, 6.6, 7.4])
intensidad_angulo_20 = np.array([6, 6.8, 7, 6.8, 6.4, 5.6, 4.8, 3.6, 2.6, 1.8, 1.2, 1, 1, 1.4, 2.2, 3, 4, 5.2, 5.8])
intensidad_angulo_30 = np.array([4.6, 5.2, 5.4, 5.8, 5.8, 5.6, 5, 4.4, 3.8, 3.2, 2.6, 2.2, 2, 2, 2.2, 2.6, 3.2, 4, 4.6])
intensidad_angulo_40 = np.array([3.8, 4, 4.2, 4.4, 4.6, 4.6, 4.6, 4.2, 4.2, 4, 3.8, 3.6, 3.2, 3.2, 3.2, 3.2, 3.2, 3.4, 3.6])
intensidad_angulo_50 = np.array([4, 3.6, 3.2, 3, 3, 3, 3, 3.2, 3.6, 4, 4.2, 4.4, 4.6, 4.6, 4.8, 4.6, 4.4, 4.2, 3.8])


plt.plot(angulos, intensidad_angulo_0, 'o-', label='0°')
plt.plot(angulos, intensidad_angulo_10, 'o-', label='10°', color='orange')
plt.plot(angulos, intensidad_angulo_20, 'o-', label='20°', color='green')
plt.plot(angulos, intensidad_angulo_30, 'o-', label='30°', color='purple')
plt.plot(angulos, intensidad_angulo_40, 'o-', label='40°', color='brown')
plt.plot(angulos, intensidad_angulo_50, 'o-', label='50°', color='magenta')

plt.title('Polarización por Birrefringencia con un Retardador')
plt.xlabel('Ángulo (grados)')
plt.ylabel('Intensidad (arbitraria)')
plt.grid()
plt.legend(loc='upper right')
plt.xlim(-9, 225)
plt.show()

# Polarización por Reflexión

angulos_cristal = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80])

intensidad_analizador_0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.8, 1, 1.2, 1.4, 1.6, 2, 2.2, 2.4, 2.6, 2.8, 3.4, 4, 4.6, 5.8])
intensidad_analizador_90 = np.array([2, 2, 2, 1.8, 1.8, 1.8, 1.6, 1.6, 1.6, 1.6, 1.4, 1.4, 1.4, 1.4, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.4, 1.4, 1.6, 2.2, 2.4, 3, 3.6, 4.4, 6])

print((48+ 50+ 52+ 54+ 56+ 58+ 60+ 62)/8)

plt.plot(angulos_cristal, intensidad_analizador_0+2, 'o-', label='Analizador 0°')
plt.plot(angulos_cristal, intensidad_analizador_90, 'o-', label='Analizador 90°', color='orange')
plt.title('Polarización por Reflexión')
plt.xlabel('Ángulo del cristal (grados)')
plt.ylabel('Intensidad (arbitraria)')
plt.grid()
plt.legend(loc='upper left')
plt.show()


# ariación de la Intensidad del Rayo Refractado con el Número de Placas

num_placas = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
intensidad_placas_0_grados = np.array([10, 9.2, 8.4, 7.6, 6.8, 6.4, 5.8, 5.4, 5, 4.6, 4.4, 4.2, 4])-4.0
intensidad_placas_45_grados = np.array([5.8, 5.4, 5, 4.6, 4.2, 4, 3.8, 3.6, 3.4, 3.2, 3.2, 3, 3])-3.0
intensidad_placas_90_grados = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2])-2.0

plt.plot(num_placas, intensidad_placas_0_grados, 'o-', label='0°')
plt.plot(num_placas, intensidad_placas_45_grados, 'o-', label='45°', color='blue')
plt.plot(num_placas, intensidad_placas_90_grados, 'o-', label='90°', color='orange')
plt.title('Variación de la Intensidad del Rayo Refractado con el Número de Placas')
plt.xlabel('Número de Placas')
plt.ylabel('Intensidad (arbitraria)')
plt.legend(loc='upper right')
plt.grid()
plt.show()
