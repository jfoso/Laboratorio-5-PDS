# Laboratorio-5-PDS
## OBJETIVO
Analizar la variabilidad de la frecuencia cardíaca (HRV) utilizando la transformada wavelet para identificar cambios en las frecuencias características y analizar la dinámica temporal de la señal cardíaca.
## Procedimiento
Para comenzar a realizar de manera efectiva el laboratorio acerca de Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet mediante el software python, debemos tener en cuenta los siguientes topicos:
### Actividad simpática y parasimpática del sistema nervioso autónomo
El sistema nervioso autónomo (SNA) es el que se encarga de regular las funciones involuntarias del cuerpo, como el ritmo cardíaco, la digestión y la respiración. Se divide en dos ramas principales con efectos generalmente opuestos:
* **Sistema Nervioso Simpático:** Este actúa como el "acelerador" del cuerpo. Se activa en situaciones de estrés, peligro o excitación física, preparando al organismo para la acción ("lucha o huida"). Sus efectos incluyen: Aumento de la frecuencia y fuerza del latido cardíaco, aumento de la frecuencia respiratoria y dilatación de los bronquios, aumento de sudoración y en algunos casos se libera adrenalina y noradrenalina
* **Sistema Nervioso Parasimpático:** Se podría decir que este actúa como el "freno" del cuerpo ya que redomina en estados de calma y relajación, en este caso se enfoca  en la conservación de energía y las funciones de "descanso y digestión". Sus efectos incluyen: Estimulación de la digestión y el aumento del flujo sanguíneo al sistema digestivo y disminución de la frecuencia cardíaca y la presión arterial.
En la mayoría de las situaciones estos dos sistemas trabajan de forma coordinada para mantener un equilibrio interno (homeostasis). La actividad de uno a menudo contrarresta la del otro, permitiendo respuestas adaptativas a diferentes estímulos a los que sea sometido. Un equilibrio saludable entre la actividad simpática y parasimpática es esencial para el bienestar general, en este caso para realizar el laboratorio se someterá al sujeto a evaluar a estimulos de relajación (actividad parasimpática) y de estrés (actividad simpática) para aumentar o disminuir su frecuencia cardiaca.
### Variabilidad de la Frecuencia Cardíaca (HRV)
Esta se refiere a las fluctuaciones en la duración del intervalo R-R, es decir el tiempo entre latidos consecutivos del corazón, no a cambios en la frecuencia cardíaca promedio en sí. Estas variaciones minuto a minuto reflejan la modulación del ritmo cardíaco por el sistema nervioso autónomo.
Para el análisis de HRV mediante la Transformada Wavelet, las frecuencias de interés que más se examinan corresponden a la actividad de los sistemas simpático y parasimpático:
* **Ondas de Alta Frecuencia (HF):** Estas se asocian con la actividad parasimpática y se encuentran en el rango de 0.15 a 0.4 Hz. Reflejan la influencia del sistema nervioso vago (nervio parasimpático) en la modulación del ritmo cardíaco, a menudo vinculadas a la respiración.

* **Ondas de Baja Frecuencia (LF):** Se cree que reflejan la influencia de ambos sistemas, simpático y parasimpático, y se encuentran en el rango de 0.04 a 0.15 Hz respectivamente. Su origen es más complejo y se asocia con mecanismos barorreceptores y termorreguladores. La relación LF/HF a menudo se utiliza como un índice del equilibrio simpático-vagal.

* **Ondas de Muy Baja Frecuencia (VLF):** Se encuentran por debajo de 0.04 Hz (típicamente 0.0033 a 0.04 Hz) y sus mecanismos fisiológicos aún no se comprenden completamente.

### Transformada Wavelet (TW)
Esta es una técnica matemática para analizar señales que cambian con el tiempo, especialmente aquellas cuyas frecuencias varían. A diferencia de la Transformada de Fourier, utiliza wavelets, que son ondículas o ondas muy pequeñas de duración limitada. La WT realiza un análisis tiempo-frecuencia, mostrando qué componentes de frecuencia están presentes y cuándo ocurren. Se logra comparando la señal con versiones escaladas y desplazadas de una wavelet madre, generando coeficientes wavelets para un mejor análisis de la señal original.Estas se utilizan para análisis de señales no estacionarias, eliminación de ruido, compresión de datos, detección de cambios bruscos y análisis de EEG, ECG, EMG para diagnóstico; procesamiento de imágenes médicas; y fundamentalmente, análisis de la Variabilidad de la Frecuencia Cardíaca (VFC) para estudiar la actividad autonómica como se realizará en el presente laboratorio, a continuación se expondran algunos tipos de Wavelet Relevantes en Señales Biológicas:
* **Haar:** Simple, buena para detectar cambios repentinos.
* **Daubechies (dbN) y Symlet (symN):** Familias versátiles con buen equilibrio entre localización temporal y frecuencial.
* **Morlet:** Compleja, excelente para análisis tiempo-frecuencia de oscilaciones y ritmos, muy usada en VFC.
* **Sombrero mexicano (Mexican Hat):** Útil para identificar picos y valles.
Al tener claros los topicos mencionados anteriormente se procede a tomar a un sujeto de prueba para medir la señal electrocardiográfica durante 5 minutos en reposo para así garantizar la reducción de ruido experimental y posterior a esos 5 minutos 3 mintos sometiendo al sujeto a audios e imagenes que causarán estrés en el mismo donde se  utilizó una frecuencia de muestreo de tatata, obteniendo la siguiente señal:**ponerseñal**


Posterior a esto se realizó un filtro FIR deacuerdo a los parametros de la señal adquirida, para asi obtener la ecuación en diferencial del filtro e implementar el filtro a la señal obtenida asumiendo parámetros iniciales en 0 respectivamente mediante el siguiente código:
```ruby
    **ponercodigo**
```
 con la itención de identificar los picos R en la señal obtenida, calcular los intervalos R-R y obtener una nueva señal como se evidencia en la siguiente imagen:
 **poner imagen**
A continuación se calculan los los parámetros básicos de la HRV en el dominio del tiempo, como la media de los intervalos R-R y su desviación estándar de la siguiente manera:
```ruby
    **ponercodigo**
```
Posterior a esto se realiza un espectrograma de la HRV usando la transformada wavelet en este caso **continua o discreta**, utilizando la función wavelet **tatata** con frecuecias de **tatata**, obteniendo el siguiente resultado:
**poner imagen**

## Resultados obtenidos

