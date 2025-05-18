"""
Módulo para medir y recopilar tiempos de ejecución de los algoritmos de pattern matching.
"""

import time
from typing import Dict, List, Callable, Tuple, Any

from .data_generator import generate_random_text, generate_random_pattern, set_random_seed
from .constants import RANDOM_SEED

def measure_execution_time(
    algorithm: Callable[[str, str], List[int]],
    text: str,
    pattern: str,
    num_runs: int = 1
) -> float:
    """
    Mide el tiempo de ejecución promedio de un algoritmo de pattern matching.
    
    Args:
        algorithm: Función que implementa el algoritmo a medir
        text: Texto en el que buscar el patrón
        pattern: Patrón a buscar
        num_runs: Número de veces que se ejecutará el algoritmo para promediar
        
    Returns:
        Tiempo promedio de ejecución en segundos
    """
    if num_runs <= 0:
        raise ValueError("El número de ejecuciones debe ser mayor que cero")
    
    total_time = 0.0
    
    for _ in range(num_runs):
        start_time = time.time()
        _ = algorithm(text, pattern)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    return total_time / num_runs

def run_performance_comparison(
    algorithms: Dict[str, Callable[[str, str], List[int]]],
    text_sizes: List[int],
    pattern_size: int,
    num_tests: int = 5,
    random_seed: int = RANDOM_SEED
) -> Dict[str, List[float]]:
    """
    Ejecuta una comparación de rendimiento entre varios algoritmos de pattern matching.
    
    Args:
        algorithms: Diccionario de {nombre_algoritmo: funcion_algoritmo}
        text_sizes: Lista de tamaños de texto a probar
        pattern_size: Tamaño del patrón a buscar
        num_tests: Número de pruebas para promediar los resultados
        random_seed: Semilla para el generador de números aleatorios
        
    Returns:
        Diccionario con tiempos de ejecución promedio por algoritmo y tamaño
    """
    set_random_seed(random_seed)
    results = {algo_name: [] for algo_name in algorithms.keys()}
    
    for text_size in text_sizes:
        print(f"\nProbando con tamaño de texto: {text_size}")
        
        # Generar datos para esta prueba
        pattern = generate_random_pattern(pattern_size)
        text = generate_random_text(text_size)
        
        # Medir cada algoritmo
        for algo_name, algo_func in algorithms.items():
            print(f"  Ejecutando {algo_name}...", end="", flush=True)
            
            try:
                execution_time = measure_execution_time(
                    algorithm=algo_func,
                    text=text,
                    pattern=pattern,
                    num_runs=num_tests
                )
                results[algo_name].append(execution_time)
                print(f" {execution_time:.6f} segundos")
            except Exception as e:
                print(f" ERROR: {str(e)}")
                results[algo_name].append(float('nan'))
    
    return results

def compare_algorithms_with_fixed_inputs(
    algorithms: Dict[str, Callable[[str, str], List[int]]],
    text: str,
    pattern: str,
    num_tests: int = 5
) -> Dict[str, float]:
    """
    Compara varios algoritmos utilizando un texto y patrón específicos.
    
    Args:
        algorithms: Diccionario de {nombre_algoritmo: funcion_algoritmo}
        text: Texto en el que buscar
        pattern: Patrón a buscar
        num_tests: Número de pruebas para promediar los resultados
        
    Returns:
        Diccionario con tiempos de ejecución promedio por algoritmo
    """
    results = {}
    
    for algo_name, algo_func in algorithms.items():
        print(f"Ejecutando {algo_name}...", end="", flush=True)
        
        try:
            execution_time = measure_execution_time(
                algorithm=algo_func,
                text=text,
                pattern=pattern,
                num_runs=num_tests
            )
            results[algo_name] = execution_time
            print(f" {execution_time:.6f} segundos")
        except Exception as e:
            print(f" ERROR: {str(e)}")
            results[algo_name] = float('nan')
    
    return results

def validate_algorithm_correctness(
    algorithms: Dict[str, Callable[[str, str], List[int]]],
    text: str,
    pattern: str
) -> Dict[str, bool]:
    """
    Valida que todos los algoritmos devuelvan los mismos resultados.
    
    Args:
        algorithms: Diccionario de {nombre_algoritmo: funcion_algoritmo}
        text: Texto en el que buscar
        pattern: Patrón a buscar
        
    Returns:
        Diccionario que indica si cada algoritmo devolvió resultados correctos
    """
    expected_positions = None
    results = {}
    
    for algo_name, algo_func in algorithms.items():
        positions = algo_func(text, pattern)
        
        # El primer algoritmo establece las posiciones esperadas
        if expected_positions is None:
            expected_positions = sorted(positions)
            results[algo_name] = True
        else:
            # Compara con las posiciones esperadas
            results[algo_name] = (sorted(positions) == expected_positions)
    
    return results
