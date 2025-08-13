import matplotlib.pyplot as plt
import numpy as np

"""

Experimeto 1. Introducción a la Óptica de Rayos

"""

DistanciaSensor = 1.3
Intensidad = np.array([684, 454, 292, 204, 142, 110, 81, 64, 54, 45, 38, 33, 27])
Distancia = np.array([18.5, 21.2, 24.8, 28.3, 32.5, 35.9, 40.8, 44.6, 48.1, 51.7, 55.4, 59.0, 64.1]) + DistanciaSensor

A = Intensidad[0] * (Distancia[0])**2

Intensidad_teorica = A / Distancia**2 # Usamos el primer punto como referencia

plt.plot(Distancia, Intensidad, label = 'Experimental', )
plt.plot(Distancia, Intensidad_teorica, label= 'Teórica')
plt.title('Intensidad vs Distancia')
plt.ylabel('Intensidad (Lux)')
plt.xlabel('Distancia (cm)')
plt.grid()
plt.legend()
plt.show()


PlacaRendija = 13.0
PantallaVisualizacion = np.sort(np.array([16.3, 22.8, 44.3, 32.2, 41.4, 27.7])) - PlacaRendija
AnchoLinea = np.sort(np.array([0.1, 0.4, 1.3, 0.7, 1.1, 0.6]))
DistanciaEntreLinea = np.sort(np.array([0.5, 0.8, 1.9, 1.5, 1.7, 1.0]))

plt.plot(PantallaVisualizacion, AnchoLinea, 'o-', markersize=10, label='Ancho de Línea')
plt.plot(PantallaVisualizacion, DistanciaEntreLinea, 'o-', markersize=10, c='green', label='Separacion Entre Líneas')
plt.title('Ancho de Línea y Separación Entre Líneas vs Distancia')
plt.xlabel('Distancia (cm)')
plt.grid()
plt.legend()
plt.show()

Filamento = 8.4
CentroDibujo = 29.5 - Filamento
print(CentroDibujo, 'cm', '- Medido')
DistanciaExperimental = 20.7 
print(DistanciaExperimental, 'cm', '- Trazado')
print( 'Discrepancia', (CentroDibujo-DistanciaExperimental)/CentroDibujo*100 )



"""

Experimeto 2. La Ley de la Reflexión

"""

AnguloIncidente = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])
AnguloReflejado = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])

plt.plot(AnguloIncidente, AnguloReflejado, label='Reflexión')  # Excluye el 90° para reflejado

plt.plot(AnguloIncidente[-1], AnguloReflejado[-1], 'rX', markersize=15, label='En 90° no se refleja')

plt.annotate('No hay reflexión en 90°, \n solo en valores cercanos',
             xy=(AnguloIncidente[-1], AnguloReflejado[-1]),
             xytext=(70, 55),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10,
             color='red')

plt.title('Ley de Reflexión')
plt.xlabel('Ángulo Incidente (gra)')
plt.ylabel('Ángulo Reflejado (gra)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


"""

Experimeto 3. Formación de Una Imagen en un Espejo Plano

"""

# Esta parte es hacer el trazado de rayos

Filamento = 8.4
DistanciaEspejo = 26.2 - Filamento
print(np.round(DistanciaEspejo,3), 'cm', '- Medido')
DistanciaReflejo = 17.8 
print(np.round(DistanciaReflejo,3), 'cm', '- Trazado')

print( 'Discrepancia', (DistanciaEspejo-DistanciaReflejo)/DistanciaEspejo*100 )


"""

Experimeto 4. La Ley de la Refracción

"""

AnguloIncidente = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])
AnguloRefractado = np.array([0, 7, 14, 21, 27, 33, 37, 41, 44, 45, 46])

plt.plot(AnguloIncidente, AnguloRefractado, label='Refracción')

plt.plot(AnguloIncidente[-1], AnguloRefractado[-1], 'rX', markersize=15, label='En 90° no se refleja')

plt.annotate('No hay refracción en 90°, \n solo en valores cercanos',
             xy=(AnguloIncidente[-1], AnguloRefractado[-1]),
             xytext=(60, 30),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10,
             color='red')

plt.title('Ley de Refracción')
plt.xlabel('Ángulo Incidente (gra)')
plt.ylabel('Ángulo Refractado (gra)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

"""

Experimeto 5. Reversibilidad

"""

AnguloIncidente = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])
AnguloRefractado = np.array([0, 7, 14, 20, 27, 32, 37, 41, 43, 45, 46])

plt.plot(AnguloRefractado, AnguloIncidente, label='Refracción')

plt.plot(AnguloRefractado[-1], AnguloIncidente[-1], 'rX', markersize=15, label='En 90° no se refleja')

plt.annotate('No hay refracción en 90°, \n solo en valores cercanos',
             xy=(AnguloRefractado[-1], AnguloIncidente[-1]),
             xytext=(20, 70),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10,
             color='red')

plt.title('Reversibilidad')
plt.ylabel('Ángulo Incidente (gra)')
plt.xlabel('Ángulo Refractado (gra)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

"""

Experimeto 4 y 5. Comparación

"""

AnguloIncidente = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])
AnguloRefractado = np.array([0, 7, 14, 21, 27, 33, 37, 41, 44, 45, 46])

plt.plot(AnguloIncidente, AnguloRefractado, label='Incidete-Refracción')

plt.plot(AnguloIncidente[-1], AnguloRefractado[-1], 'rX', markersize=15)


AnguloIncidente = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 85, 90])
AnguloRefractado = np.array([0, 7, 14, 20, 27, 32, 37, 41, 43, 45, 46])

plt.plot(AnguloRefractado, AnguloIncidente, label='Refracción-Incidente')

plt.plot(AnguloRefractado[-1], AnguloIncidente[-1], 'rX', markersize=15, label='En 90° no se refleja')

plt.grid(True)
plt.title('Ley de Refracción y Reversibilidad')
plt.xlim(-4, 100)
plt.ylim(-4, 100)
plt.tight_layout()
plt.gca().set_aspect('equal')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

"""

Experimeto 6. Reflexión Interna Total

"""

# Esta parte es observacional