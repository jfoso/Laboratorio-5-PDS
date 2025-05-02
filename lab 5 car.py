import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
from scipy.signal import butter, filtfilt, find_peaks

# === 1. Cargar señal ECG ===
data = pd.read_csv('C:\\Users\\sachi\\OneDrive - unimilitar.edu.co\\Sexto semestre\\Lab señales\\lab 5\\ecg saamtiago.csv')
ecg = data.iloc[:, 1].values
tiempo = data.iloc[:, 0].values
tiempo = tiempo - tiempo[0]  
fs = 100  

# === 2. Filtro pasa banda IIR ===
lowcut = 0.5
highcut = 40.0
order = 4
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(order, [low, high], btype='band')
ecg_filtrado = filtfilt(b, a, ecg)

# === 3. Detección de Picos R ===
umbral = np.percentile(ecg_filtrado, 75)
distancia_minima = int(fs * 0.4)
prominencia_minima = 0.5

picos_r, propiedades = find_peaks(ecg_filtrado, height=umbral, distance=distancia_minima, prominence=prominencia_minima)

print(f"Picos R detectados: {len(picos_r)}")

# === 4. Calcular intervalos R-R ===
if len(picos_r) > 1:
    rr_intervals = np.diff(tiempo[picos_r])
else:
    rr_intervals = np.array([])

# === 5. Métricas HRV ===
media_rr = np.mean(rr_intervals)
std_rr = np.std(rr_intervals)
rr_min = np.min(rr_intervals) if rr_intervals.size > 0 else 0
rr_max = np.max(rr_intervals) if rr_intervals.size > 0 else 0

print("Parámetros de HRV:")
print(f" - Media R-R: {media_rr:.4f} s")
print(f" - Desviación estándar: {std_rr:.4f} s")
print(f" - Mínimo R-R: {rr_min:.4f} s")
print(f" - Máximo R-R: {rr_max:.4f} s")

# === 6. Graficar ECG con Picos R ===
plt.figure(figsize=(10, 5))
plt.plot(tiempo, ecg_filtrado, label='ECG Filtrado', color='blue')
plt.plot(tiempo[picos_r], ecg_filtrado[picos_r], 'ro', label='Picos R')
plt.title('ECG Filtrado con Picos R')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend()
plt.grid(True)
plt.show()

# === 7. Graficar Intervalos R-R ===
plt.figure(figsize=(10, 4))
plt.plot(rr_intervals, marker='o')
plt.title('Intervalos R-R')
plt.xlabel('Tiempo del pico R anterior (s)')
plt.ylabel('Intervalo (s)')
plt.grid(True)
plt.show()

# === 8. Transformada Wavelet de Morlet ===
scales = np.arange(1, 64)
waveletname = 'cmor1.5-1.0'  

coeficientes, frecuencias = pywt.cwt(ecg_filtrado, scales, waveletname, sampling_period=1/fs)

# === 9. Graficar Transformada Wavelet ===
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(coeficientes), extent=[tiempo[0], tiempo[-1], scales[-1], scales[0]],
           cmap='jet', aspect='auto')
plt.title('Transformada Wavelet de Morlet (ECG)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.colorbar(label='Magnitud')
plt.grid(True)
plt.show()
