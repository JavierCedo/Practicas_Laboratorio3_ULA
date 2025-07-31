import numpy as np
import matplotlib.pyplot as plt

# --- Parte 1: Experimentos con películas delgadas de espesor variable (Cuña de Aire) ---

print("--- Cálculos para la Cuña de Aire (Papel) ---")

x_papel = np.array([
    20.27, 20.22, 20.17, 20.13, 20.08,
    20.04, 20.00, 19.96, 19.90, 19.86,
    19.82, 19.77, 19.73, 19.68, 19.64,
    19.59, 19.55, 19.50, 19.46, 19.42,
    19.37, 19.32, 19.28, 19.24, 19.19,
    19.14, 19.09, 19.05, 19.01, 18.97
]) * 1e-3  # m

lambda_sodio = 589.3e-9  # m
L_papel = 4.115 * 1e-2  # m

delta_x_papel = np.abs(np.diff(x_papel))
avg_delta_x_papel = np.mean(delta_x_papel)
print(f"Espaciado promedio deltax (papel): {avg_delta_x_papel:.5e} m")


# Ecuación (8-10): d = Lλ / (2Δx)
d_calculado_papel = L_papel * lambda_sodio / (2 * avg_delta_x_papel)
print(f"Espesor calculado (papel): {d_calculado_papel:.4e} m")

alpha_rad_papel = np.arctan(d_calculado_papel / L_papel)
print(f"Ángulo óptico (cuña de aire, papel): {alpha_rad_papel:.4e} rad ({np.degrees(alpha_rad_papel):.4f}°)")
print('el que busco', alpha_rad_papel, np.degrees(alpha_rad_papel))
d_experimental_papel_tab = 0.28e-3
d_experimental_papel_med = 0.21e-3

print(f"Espesor tabulado (papel): {d_experimental_papel_tab:.4e} m")
print(f"Discrepancia con tabulado: {np.abs(d_calculado_papel - d_experimental_papel_tab)/d_experimental_papel_tab*100:.2f} %")

print(f"Espesor medido (papel): {d_experimental_papel_med:.4e} m")

print(f"Discrepancia con medido: {np.abs(d_calculado_papel - d_experimental_papel_med)/d_experimental_papel_med*100:.2f} %")

alpha_geom_papel = np.arctan(d_experimental_papel_med / L_papel)
print(f"Ángulo geométrico (medido): {np.degrees(alpha_geom_papel):.4f}°")

print("-" * 40)
print("--- Cálculos para la Cuña de Aire (Cabello) ---")

x_cabello = np.array([
    12.42, 12.29, 12.16, 12.04, 11.91,
    11.78, 11.64, 11.50, 11.37, 11.24,
    11.10, 10.98, 10.84, 10.70, 10.56,
    10.42, 10.28, 10.14, 10.02, 9.88,
    9.74, 9.60, 9.48, 9.32, 9.19,
    9.06, 8.91, 8.79, 8.66, 8.52, 8.38
]) * 1e-3

L_cabello = 4.265 * 1e-2  # m

delta_x_cabello = np.abs(np.diff(x_cabello))
avg_delta_x_cabello = np.mean(delta_x_cabello)
print(f"Espaciado promedio deltax (cabello): {avg_delta_x_cabello:.5e} m")

d_calculado_cabello = L_cabello * lambda_sodio / (2 * avg_delta_x_cabello)
print(f"Diámetro calculado (cabello): {d_calculado_cabello:.4e} m")

alpha_rad_cabello = np.arctan(d_calculado_cabello / L_cabello)
print(f"Ángulo óptico (cabello): {alpha_rad_cabello:.4e} rad ({np.degrees(alpha_rad_cabello):.4f}°)")
print('el que busco', alpha_rad_cabello, np.degrees(alpha_rad_cabello))

d_experimental_cabello_tab = 0.09e-3
d_experimental_cabello_med = 0.07e-3

print(f"Diámetro tabulado (cabello): {d_experimental_cabello_tab:.4e} m")
print(f"Discrepancia con tabulado: {np.abs(d_calculado_cabello - d_experimental_cabello_tab)/d_experimental_cabello_tab*100:.2f} %")

print(f"Diámetro medido (cabello): {d_experimental_cabello_med:.4e} m")
print(f"Discrepancia con medido: {np.abs(d_calculado_cabello - d_experimental_cabello_med)/d_experimental_cabello_med*100:.2f} %")

print("=" * 40)

# --- Parte 2: Anillos de Newton con ANILLOS BRILLANTES ---

lambda_sodio = 589.3e-9  # m

print("\n--- Cálculos para Anillos de Newton (Lente 1) ---")

x_izq_lente1 = np.array([7.38, 7.59, 7.76, 7.89, 7.98, 8.08, 8.17, 8.23, 8.28, 8.35]) * 1e-3
x_der_lente1 = np.array([6.74, 6.51, 6.37, 6.25, 6.16, 6.05, 5.96, 5.89, 5.81, 5.75]) * 1e-3

m1 = np.arange(1, len(x_izq_lente1) + 1) + 0.5  # Para anillos brillantes
r1 = np.abs(x_izq_lente1 - x_der_lente1) / 2
r1_squared = r1 ** 2

pend1, interc1 = np.polyfit(m1, r1_squared, 1)
R1 = pend1 / lambda_sodio
print(f"Radio de curvatura R1 (anillos brillantes): {R1:.5f} m")

plt.figure()
plt.plot(m1, r1_squared, 'bo', label='Datos')
plt.plot(m1, pend1 * m1 + interc1, 'r-')
plt.xlabel('$m + 0.5$ (número de anillo brillante)')
plt.ylabel('$r_m^2$ (m²)')
plt.title('Anillos de Newton - Lente 1')
plt.legend()
plt.grid(True)
plt.tight_layout()

# --- Lente 2 ---
print("\n--- Cálculos para Anillos de Newton (Lente 2) ---")

x_izq_lente2 = np.array([8.83, 9.11, 9.30, 9.46, 9.61, 9.74, 9.84, 9.96, 10.05, 10.17]) * 1e-3
x_der_lente2 = np.array([8.07, 7.77, 7.57, 7.42, 7.25, 7.14, 7.02, 6.91, 6.80, 6.71]) * 1e-3

m2 = np.arange(1, len(x_izq_lente2) + 1) + 0.5
r2 = np.abs(x_izq_lente2 - x_der_lente2) / 2
r2_squared = r2 ** 2

pend2, interc2 = np.polyfit(m2, r2_squared, 1)
R2 = pend2 / lambda_sodio
print(f"Radio de curvatura R2 (anillos brillantes): {R2:.5f} m")

plt.figure()
plt.plot(m2, r2_squared, 'bo', label='Datos')
plt.plot(m2, pend2 * m2 + interc2, 'r-')
plt.xlabel('$m + 0.5$ (número de anillo brillante)')
plt.ylabel('$r_m^2$ (m²)')
plt.title('Anillos de Newton - Lente 2')
plt.legend()
plt.grid(True)
plt.tight_layout()

# --- Lente 3 ---
print("\n--- Cálculos para Anillos de Newton (Lente 3) ---")

x_izq_lente3 = np.array([10.56, 10.67, 10.81, 10.90, 10.99, 11.05, 11.13, 11.20, 11.25, 11.31]) * 1e-3
x_der_lente3 = np.array([9.96, 9.79, 9.66, 9.55, 9.49, 9.40, 9.33, 9.27, 9.21, 9.16]) * 1e-3

m3 = np.arange(1, len(x_izq_lente3) + 1) + 0.5
r3 = np.abs(x_izq_lente3 - x_der_lente3) / 2
r3_squared = r3 ** 2

pend3, interc3 = np.polyfit(m3, r3_squared, 1)
R3 = pend3 / lambda_sodio
print(f"Radio de curvatura R3 (anillos brillantes): {R3:.5f} m")

plt.figure()
plt.plot(m3, r3_squared, 'bo', label='Datos')
plt.plot(m3, pend3 * m3 + interc3, 'r-')
plt.xlabel('$m + 0.5$ (número de anillo brillante)')
plt.ylabel('$r_m^2$ (m²)')
plt.title('Anillos de Newton - Lente 3')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()


t = (600*10**(-9))/(1.33*4)
print(t)
