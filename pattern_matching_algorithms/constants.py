"""
Constantes utilizadas en todo el proyecto de pattern matching.
"""

# Tamaños por defecto para textos y patrones
DEFAULT_TEXT_SIZE = 100000
DEFAULT_PATTERN_SIZE = 10
DEFAULT_NUM_TESTS = 5

# Caracteres disponibles para generar textos aleatorios
# Por defecto, utilizamos el alfabeto inglés (mayúsculas y minúsculas)
DEFAULT_CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Semilla para generador de números aleatorios (para reproducibilidad)
RANDOM_SEED = 42

# Tamaño máximo recomendado para textos (para evitar problemas de memoria)
MAX_RECOMMENDED_TEXT_SIZE = 10000000  # 10MB

# Constantes para la visualización
ALGORITHM_COLORS = {
    "Fuerza Bruta": "blue",
    "Knuth-Morris-Pratt": "red",
    "Boyer-Moore": "green",
    "Rabin-Karp": "purple",
    "Aho-Corasick": "orange"
}

# Constante para número primo grande (utilizado en el algoritmo de Rabin-Karp)
LARGE_PRIME = 1000000007
