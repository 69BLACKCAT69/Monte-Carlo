# Monte-Carlo
Este proyecto simula el comportamiento de una fila de atención al cliente, como en un banco o tienda, usando números generados por computadora. Analiza cuánto esperan las personas y cuánto tardan en ser atendidas, basándose en datos reales de tiempos de llegada y servicio. Los resultados ayudan a entender y mejorar la eficiencia del sistema.

# 📊 Simulación de Sistemas de Colas con Generadores Pseudoaleatorios

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🌟 Descripción del Proyecto

Un sistema de simulación completo que modela procesos de colas en entornos de servicio (bancos, hospitales, retail) mediante:

- 🔢 **Generación de números pseudoaleatorios** con método congruencial lineal mejorado
- ⏱ **Modelado estadístico** de tiempos de llegada y servicio
- 📈 **Análisis de métricas** operacionales del sistema

## 🧩 Componentes Principales

### 1. Generadores Pseudoaleatorios
```python
def generador_numeros_pseudoaleatorios(x0, a, m, c):
    # Implementación del método congruencial lineal
    xn = (a * x0 + c) % m
    return xn / m
```

### 2. Modelos de Distribución
- `Tiempo_Llegada.xlsx`: Frecuencias observadas de llegada de clientes
- `Tiempo_Servicio.xlsx`: Distribución de tiempos de atención

## 🛠 Instalación y Uso

1. **Requisitos**:
   ```bash
   pip install pandas openpyxl
   ```

2. **Ejecución**:
   ```bash
   python SIMULACIÓN.py
   ```

3. **Opciones**:
   ```
   [1] Generar N números pseudoaleatorios
   [2] Generar hasta completar período
   ```

## 📊 Estructura de Archivos

```
📦 proyecto-simulacion
├── 📄 SIMULACIÓN-1.py          # Script principal
├── 📊 Tiempo_Llegada.xlsx      # Datos de llegadas
├── 📊 Tiempo_Servicio.xlsx     # Datos de servicio
├── 📄 numeros.txt              # Resultados generados
└── 📄 MONTE CARLO.py           # Generador tiempos
```

## 📌 Características Clave

✔ **Generación robusta** de números pseudoaleatorios  
✔ **Validación automática** de parámetros  
✔ **Interfaz interactiva** para configuración  
✔ **Exportación de resultados** para análisis posterior  
✔ **Modelado basado** en datos empíricos reales  

## 📈 Métricas Calculadas

| Métrica               | Fórmula                     | Descripción                  |
|-----------------------|----------------------------|-----------------------------|
| Tiempo en cola        | ∑(T_llegada - T_servicio) | Espera promedio por cliente |
| Utilización           | T_servicio/T_total        | % uso del servidor          |
| Longitud de cola      | Clientes_en_espera        | Promedio en periodo        |

## 📝 Ejemplo de Uso

```python
# Cargar distribución de tiempos
df_llegadas = pd.read_excel('Tiempo_Llegada.xlsx')

# Generar tiempo entre llegadas
def generar_tiempo(rnd):
    for index, row in df_llegadas.iterrows():
        if rnd <= row['Frecuencia Acum']:
            return row['T. DE LLEGADA(MIN)']
```

## 📚 Documentación Adicional

- [Teoría de Colas](https://es.wikipedia.org/wiki/Teoría_de_colas)
- [Métodos Pseudoaleatorios](https://www.sciencedirect.com/topics/computer-science/pseudo-random-number)

## ✉ Contacto

¿Preguntas o sugerencias?  
📧 contacto@example.com  
🔗 [github.com/tuperfil](https://github.com/tuperfil)

---

> "La simulación es el arte de comprender sistemas complejos mediante modelos computacionales" - John Doe
