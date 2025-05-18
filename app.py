#!/usr/bin/env python3
"""
Aplicación principal para el proyecto de pattern matching.
Proporciona una interfaz para ejecutar algoritmos de coincidencia de patrones
y visualizar los resultados comparativos.
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from typing import Dict, List, Tuple

from pattern_matching_algorithms.algorithms import (
    brute_force, 
    knuth_morris_pratt, 
    boyer_moore, 
    rabin_karp,
    aho_corasick
)
from pattern_matching_algorithms.data_generator import (
    generate_random_text,
    generate_random_pattern
)
from pattern_matching_algorithms.execution_time_gathering import (
    measure_execution_time,
    run_performance_comparison
)
from pattern_matching_algorithms.constants import (
    DEFAULT_TEXT_SIZE,
    DEFAULT_PATTERN_SIZE,
    DEFAULT_NUM_TESTS
)

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Comparación de algoritmos de Pattern Matching'
    )
    parser.add_argument(
        '--text-size', 
        type=int, 
        default=DEFAULT_TEXT_SIZE,
        help=f'Tamaño del texto (predeterminado: {DEFAULT_TEXT_SIZE})'
    )
    parser.add_argument(
        '--pattern-size', 
        type=int, 
        default=DEFAULT_PATTERN_SIZE,
        help=f'Tamaño del patrón (predeterminado: {DEFAULT_PATTERN_SIZE})'
    )
    parser.add_argument(
        '--num-tests', 
        type=int, 
        default=DEFAULT_NUM_TESTS,
        help=f'Número de pruebas a ejecutar (predeterminado: {DEFAULT_NUM_TESTS})'
    )
    parser.add_argument(
        '--save-charts', 
        action='store_true',
        help='Guardar los gráficos generados en el directorio img/'
    )
    return parser.parse_args()

def save_chart(fig, filename: str) -> None:
    """Guarda un gráfico en el directorio img/."""
    img_dir = os.path.join(os.path.dirname(__file__), 'img')
    os.makedirs(img_dir, exist_ok=True)
    fig.savefig(os.path.join(img_dir, filename), dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como {filename}")

def plot_results(results: Dict[str, List[float]], text_sizes: List[int], 
                 pattern_size: int, save: bool = False) -> None:
    """
    Grafica los resultados de tiempo de ejecución para diferentes algoritmos.
    
    Args:
        results: Diccionario con nombres de algoritmos y sus tiempos
        text_sizes: Lista de tamaños de texto utilizados
        pattern_size: Tamaño del patrón utilizado
        save: Si es True, guarda el gráfico en el directorio img/
    """
    plt.figure(figsize=(12, 8))
    
    for algorithm, times in results.items():
        plt.plot(text_sizes, times, marker='o', label=algorithm)
    
    plt.xlabel('Tamaño del Texto')
    plt.ylabel('Tiempo de Ejecución (ms)')
    plt.title(f'Comparación de Rendimiento de Algoritmos de Pattern Matching\nTamaño del Patrón: {pattern_size}')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    
    if save:
        save_chart(plt.gcf(), f'comparison_pattern{pattern_size}.png')
    
    plt.show()

def main() -> None:
    """Función principal del programa."""
    args = parse_arguments()
    
    # Definir los algoritmos a comparar
    algorithms = {
        'Fuerza Bruta': brute_force,
        'Knuth-Morris-Pratt': knuth_morris_pratt,
        'Boyer-Moore': boyer_moore,
        'Rabin-Karp': rabin_karp,
        'Aho-Corasick': aho_corasick
    }
    
    print(f"Ejecutando comparación con tamaño de texto {args.text_size}, "
          f"tamaño de patrón {args.pattern_size}, y {args.num_tests} pruebas...")
    
    # Ejecutar pruebas de rendimiento
    text_sizes = [1000, 10000, 100000, 1000000]
    pattern_size = args.pattern_size
    
    results = run_performance_comparison(
        algorithms=algorithms,
        text_sizes=text_sizes,
        pattern_size=pattern_size,
        num_tests=args.num_tests
    )
    
    # Mostrar resultados en forma tabular
    print("\nResultados de tiempo de ejecución (ms):")
    print("-" * 80)
    print(f"{'Algoritmo':<20} | " + " | ".join(f"{size:<10}" for size in text_sizes))
    print("-" * 80)
    
    for algo_name, times in results.items():
        times_ms = [t * 1000 for t in times]  # Convertir a milisegundos
        print(f"{algo_name:<20} | " + " | ".join(f"{t:<10.4f}" for t in times_ms))
    
    # Visualizar resultados
    plot_results(
        {k: [t * 1000 for t in v] for k, v in results.items()},  # Convertir a ms
        text_sizes,
        pattern_size,
        save=args.save_charts
    )

if __name__ == "__main__":
    main()
