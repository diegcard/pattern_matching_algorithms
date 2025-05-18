"""
Pruebas unitarias para el generador de datos.
"""

import unittest
import random
from typing import List

from pattern_matching_algorithms.data_generator import (
    generate_random_text,
    generate_random_pattern,
    generate_text_with_pattern,
    generate_worst_case_text,
    set_random_seed
)
from pattern_matching_algorithms.constants import DEFAULT_CHAR_SET, RANDOM_SEED

class TestDataGenerator(unittest.TestCase):
    """Pruebas para el generador de datos."""
    
    def setUp(self):
        """Preparar datos para las pruebas."""
        set_random_seed(RANDOM_SEED)
    
    def test_generate_random_text(self):
        """Prueba la generación de texto aleatorio."""
        # Probar diferentes tamaños
        sizes = [1, 10, 100, 1000]
        for size in sizes:
            with self.subTest(size=size):
                text = generate_random_text(size)
                self.assertEqual(len(text), size, 
                                f"El texto generado debe tener longitud {size}")
                
                # Verificar que todos los caracteres están en el conjunto por defecto
                for char in text:
                    self.assertIn(char, DEFAULT_CHAR_SET, 
                                 f"El carácter {char} no está en el conjunto por defecto")
        
        # Probar con un conjunto de caracteres personalizado
        custom_charset = "123"
        text = generate_random_text(100, custom_charset)
        for char in text:
            self.assertIn(char, custom_charset, 
                         f"El carácter {char} no está en el conjunto personalizado")
        
        # Probar con tamaño inválido
        with self.assertRaises(ValueError):
            generate_random_text(0)
        with self.assertRaises(ValueError):
            generate_random_text(-10)
    
    def test_generate_random_pattern(self):
        """Prueba la generación de patrones aleatorios."""
        # Verificar que es esencialmente igual a generate_random_text
        sizes = [1, 5, 10, 20]
        for size in sizes:
            with self.subTest(size=size):
                pattern = generate_random_pattern(size)
                self.assertEqual(len(pattern), size, 
                                f"El patrón generado debe tener longitud {size}")
                
                # Verificar que todos los caracteres están en el conjunto por defecto
                for char in pattern:
                    self.assertIn(char, DEFAULT_CHAR_SET, 
                                 f"El carácter {char} no está en el conjunto por defecto")
        
        # Probar con tamaño inválido
        with self.assertRaises(ValueError):
            generate_random_pattern(0)
        with self.assertRaises(ValueError):
            generate_random_pattern(-5)
    
    def test_generate_text_with_pattern(self):
        """Prueba la generación de texto con un patrón específico."""
        pattern = "ABC"
        text_size = 100
        occurrences = 5
        
        # Generar texto con el patrón
        text, positions = generate_text_with_pattern(text_size, pattern, occurrences)
        
        # Verificar tamaño del texto
        self.assertEqual(len(text), text_size, 
                        f"El texto generado debe tener longitud {text_size}")
        
        # Verificar número de ocurrencias
        self.assertEqual(len(positions), occurrences, 
                        f"Debe haber {occurrences} ocurrencias del patrón")
        
        # Verificar que el patrón está en las posiciones indicadas
        for pos in positions:
            self.assertEqual(text[pos:pos + len(pattern)], pattern, 
                            f"El patrón no está en la posición {pos}")
        
        # Verificar parámetros inválidos
        with self.assertRaises(ValueError):
            generate_text_with_pattern(0, pattern, occurrences)
        with self.assertRaises(ValueError):
            generate_text_with_pattern(text_size, pattern, 0)
        with self.assertRaises(ValueError):
            generate_text_with_pattern(5, pattern, 10)  # Texto demasiado pequeño
    
    def test_generate_worst_case_text(self):
        """Prueba la generación de textos para el peor caso de los algoritmos."""
        text_size = 1000
        pattern_size = 10
        
        # Probar con diferentes algoritmos
        algorithms = ["brute_force", "kmp", "boyer_moore", "rabin_karp"]
        
        for algo in algorithms:
            with self.subTest(algorithm=algo):
                text, pattern = generate_worst_case_text(algo, text_size, pattern_size)
                
                # Verificar tamaños
                self.assertEqual(len(text), text_size, 
                                f"El texto debe tener longitud {text_size}")
                self.assertEqual(len(pattern), pattern_size, 
                                f"El patrón debe tener longitud {pattern_size}")
                
                # Verificar que el caso sea realmente difícil (dependiendo del algoritmo)
                if algo == "brute_force":
                    # Para fuerza bruta: patrón casi coincide en cada posición
                    self.assertEqual(pattern[:pattern_size-1], "A" * (pattern_size-1))
                    self.assertEqual(pattern[-1], "B")
                
                elif algo in ["kmp", "knuth_morris_pratt"]:
                    # Para KMP: patrón con muchos prefijos parciales
                    self.assertEqual(pattern, "A" * pattern_size)
                
                elif algo in ["boyer_moore", "boyer-moore"]:
                    # Para Boyer-Moore: texto y patrón que fuerzan desplazamientos pequeños
                    self.assertEqual(pattern[:pattern_size-1], "A" * (pattern_size-1))
                    self.assertEqual(pattern[-1], "B")
                
                elif algo in ["rabin_karp", "rabin-karp"]:
                    # Para Rabin-Karp: muchas falsas alarmas de hash
                    self.assertEqual(pattern, "A" * pattern_size)
        
        # Probar con algoritmo desconocido (debería devolver texto y patrón aleatorios)
        text, pattern = generate_worst_case_text("algoritmo_desconocido", text_size, pattern_size)
        self.assertEqual(len(text), text_size)
        self.assertEqual(len(pattern), pattern_size)

if __name__ == '__main__':
    unittest.main()
