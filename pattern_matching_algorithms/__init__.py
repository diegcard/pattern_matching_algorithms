"""
Módulo principal para algoritmos de coincidencia de patrones (pattern matching).

Este módulo proporciona implementaciones de varios algoritmos de pattern matching
y herramientas para generar datos de prueba y medir su rendimiento.
"""

from .algorithms import (
    brute_force,
    knuth_morris_pratt,
    boyer_moore,
    rabin_karp,
    aho_corasick
)

from .data_generator import (
    generate_random_text,
    generate_random_pattern
)

from .execution_time_gathering import (
    measure_execution_time,
    run_performance_comparison
)

__all__ = [
    'brute_force',
    'knuth_morris_pratt',
    'boyer_moore',
    'rabin_karp',
    'aho_corasick',
    'generate_random_text',
    'generate_random_pattern',
    'measure_execution_time',
    'run_performance_comparison'
]
