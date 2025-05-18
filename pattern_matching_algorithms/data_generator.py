"""
Módulo para generar datos de prueba para algoritmos de pattern matching.
"""

import random
import string
from typing import List, Tuple, Optional

from .constants import DEFAULT_CHAR_SET, RANDOM_SEED

def set_random_seed(seed: int = RANDOM_SEED) -> None:
    """
    Establece una semilla para el generador de números aleatorios.
    
    Args:
        seed: Semilla numérica para inicializar el generador de números aleatorios
    """
    random.seed(seed)

def generate_random_text(size: int, char_set: str = DEFAULT_CHAR_SET) -> str:
    """
    Genera un texto aleatorio de un tamaño específico.
    
    Args:
        size: Tamaño del texto a generar
        char_set: Conjunto de caracteres a utilizar
        
    Returns:
        Un string con caracteres aleatorios del conjunto especificado
    """
    if size <= 0:
        raise ValueError("El tamaño del texto debe ser mayor que cero")
    
    return ''.join(random.choice(char_set) for _ in range(size))

def generate_random_pattern(size: int, char_set: str = DEFAULT_CHAR_SET) -> str:
    """
    Genera un patrón aleatorio de un tamaño específico.
    
    Args:
        size: Tamaño del patrón a generar
        char_set: Conjunto de caracteres a utilizar
        
    Returns:
        Un string con caracteres aleatorios del conjunto especificado
    """
    if size <= 0:
        raise ValueError("El tamaño del patrón debe ser mayor que cero")
    
    return generate_random_text(size, char_set)

def generate_text_with_pattern(
    text_size: int, 
    pattern: str, 
    occurrences: int = 1,
    char_set: str = DEFAULT_CHAR_SET
) -> Tuple[str, List[int]]:
    """
    Genera un texto aleatorio que contiene un patrón específico.
    
    Args:
        text_size: Tamaño total del texto a generar
        pattern: Patrón a insertar en el texto
        occurrences: Número de veces que el patrón debe aparecer
        char_set: Conjunto de caracteres a utilizar
        
    Returns:
        Una tupla (texto, posiciones) donde:
        - texto: es el texto generado
        - posiciones: es una lista con las posiciones donde se insertó el patrón
    """
    if text_size <= 0:
        raise ValueError("El tamaño del texto debe ser mayor que cero")
    
    if occurrences <= 0:
        raise ValueError("El número de ocurrencias debe ser mayor que cero")
    
    pattern_len = len(pattern)
    
    if text_size < pattern_len * occurrences:
        raise ValueError("El texto es demasiado pequeño para contener todas las ocurrencias del patrón")
    
    # Generar texto base aleatorio
    text = list(generate_random_text(text_size, char_set))
    
    # Determinar posiciones donde insertar el patrón
    available_positions = list(range(text_size - pattern_len + 1))
    positions = sorted(random.sample(available_positions, occurrences))
    
    # Insertar el patrón en las posiciones seleccionadas
    for pos in positions:
        text[pos:pos + pattern_len] = pattern
    
    return ''.join(text), positions

def generate_worst_case_text(algorithm: str, text_size: int, pattern_size: int) -> Tuple[str, str]:
    """
    Genera un texto y un patrón que representan el peor caso para un algoritmo específico.
    
    Args:
        algorithm: Nombre del algoritmo ("brute_force", "kmp", "boyer_moore", "rabin_karp")
        text_size: Tamaño del texto
        pattern_size: Tamaño del patrón
        
    Returns:
        Tupla (texto, patrón) optimizada para el peor caso del algoritmo
    """
    if algorithm.lower() == "brute_force":
        # Para fuerza bruta: patrón casi coincide, pero último carácter falla siempre
        pattern = "A" * (pattern_size - 1) + "B"
        text = ("A" * (pattern_size - 1) + "C") * (text_size // pattern_size)
        return text, pattern
    
    elif algorithm.lower() in ("kmp", "knuth_morris_pratt"):
        # Para KMP: patrón con muchos prefijos parciales
        pattern = "A" * pattern_size
        text = "A" * text_size
        return text, pattern
    
    elif algorithm.lower() in ("boyer_moore", "boyer-moore"):
        # Para Boyer-Moore: hacer que tenga que desplazarse de uno en uno
        pattern = "A" * (pattern_size - 1) + "B"
        text = "A" * text_size
        return text, pattern
    
    elif algorithm.lower() in ("rabin_karp", "rabin-karp"):
        # Para Rabin-Karp: muchas falsas alarmas de hash
        pattern = "A" * pattern_size
        text = "A" * text_size
        return text, pattern
    
    else:
        # Caso por defecto: texto y patrón aleatorios
        text = generate_random_text(text_size)
        pattern = generate_random_pattern(pattern_size)
        return text, pattern
