# Proyecto de Pattern Matching

Este proyecto implementa y compara diferentes algoritmos de pattern matching (coincidencia de patrones) en Python.

## Estructura del Proyecto

```
├── Readme.md                            # Este archivo
├── app.py                               # Aplicación principal
├── img/                                 # Directorio para imágenes y gráficos
├── pattern_matching_algorithms/         # Módulo principal
│   ├── __init__.py                      # Inicializador del módulo
│   ├── algorithms.py                    # Implementaciones de algoritmos
│   ├── constants.py                     # Constantes utilizadas en el proyecto
│   ├── data_generator.py                # Generador de datos para pruebas
│   └── execution_time_gathering.py      # Recopilación de tiempos de ejecución
└── test/                                # Pruebas unitarias
    ├── __init__.py                      # Inicializador del módulo de pruebas
    ├── test_algorithms.py               # Pruebas para los algoritmos
    └── test_data_generator.py           # Pruebas para el generador de datos
```

## Descripción

Este proyecto implementa varios algoritmos de coincidencia de patrones (pattern matching) y proporciona herramientas para comparar su rendimiento utilizando conjuntos de datos generados.

Los algoritmos implementados incluyen:
- Fuerza bruta
- Knuth-Morris-Pratt (KMP)
- Boyer-Moore
- Rabin-Karp
- Algoritmo de Aho-Corasick

## Uso

Para ejecutar la aplicación principal:

```bash
python app.py
```

Para ejecutar las pruebas:

```bash
python -m unittest discover -s test
```

## Resultados

(Aquí se incluirán gráficos comparativos de rendimiento generados a partir de las pruebas)

## Requisitos

- Python 3.8+
- Matplotlib (para gráficos)
- NumPy (para análisis de datos)

-------------------------------------------------------------------------------- 
Algoritmo            | 1000       | 10000      | 100000     | 1000000
-------------------------------------------------------------------------------- 
Fuerza Bruta         | 0.3320     | 1.0026     | 10.6685    | 106.6128
Knuth-Morris-Pratt   | 0.0000     | 0.6704     | 6.6700     | 64.3332
Boyer-Moore          | 0.0000     | 0.6642     | 4.6644     | 46.6673
Rabin-Karp           | 0.3320     | 2.6624     | 24.3333    | 242.9995
Aho-Corasick         | 0.0000     | 0.6656     | 6.6665     | 65.3336

## Licencia

MIT
