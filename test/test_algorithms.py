"""
Pruebas unitarias para los algoritmos de pattern matching.
"""

import unittest
from typing import List, Callable

from pattern_matching_algorithms.algorithms import (
    brute_force,
    knuth_morris_pratt,
    boyer_moore,
    rabin_karp,
    aho_corasick
)

class TestPatternMatchingAlgorithms(unittest.TestCase):
    """Pruebas para los algoritmos de pattern matching."""
    
    def setUp(self):
        """Preparar datos para las pruebas."""
        self.algorithms = {
            'Fuerza Bruta': brute_force,
            'Knuth-Morris-Pratt': knuth_morris_pratt,
            'Boyer-Moore': boyer_moore,
            'Rabin-Karp': rabin_karp,
            'Aho-Corasick': aho_corasick
        }
        
        # Casos de prueba básicos
        self.test_cases = [
            {
                'text': 'ABABDABACDABABCABAB',
                'pattern': 'ABABCABAB',
                'expected': [10]
            },
            {
                'text': 'AAAAAAAAAA',
                'pattern': 'AAA',
                'expected': [0, 1, 2, 3, 4, 5, 6, 7]
            },
            {
                'text': 'AAAAABAAABA',
                'pattern': 'AAAA',
                'expected': [0, 1]
            },
            {
                'text': 'ABRACADABRA',
                'pattern': 'ABRA',
                'expected': [0, 7]
            },
            {
                'text': 'ABRACADABRA',
                'pattern': 'CADA',
                'expected': [4]
            },
            {
                'text': 'ABRACADABRA',
                'pattern': 'XYZ',
                'expected': []
            },
            {
                'text': '',
                'pattern': 'ABC',
                'expected': []
            },
            {
                'text': 'ABC',
                'pattern': '',
                'expected': []
            }
        ]
    
    def test_all_algorithms(self):
        """Prueba todos los algoritmos con los casos de prueba básicos."""
        for algo_name, algo_func in self.algorithms.items():
            for i, case in enumerate(self.test_cases):
                with self.subTest(algorithm=algo_name, case=i):
                    result = algo_func(case['text'], case['pattern'])
                    self.assertEqual(result, case['expected'],
                                    f"{algo_name} falló con el caso {i}. "
                                    f"Esperado: {case['expected']}, Obtenido: {result}")
    
    def test_large_text(self):
        """Prueba los algoritmos con un texto grande."""
        large_text = "A" * 10000 + "B" + "A" * 10000
        pattern = "B"
        expected = [10000]
        
        for algo_name, algo_func in self.algorithms.items():
            with self.subTest(algorithm=algo_name):
                result = algo_func(large_text, pattern)
                self.assertEqual(result, expected,
                               f"{algo_name} falló con texto grande. "
                               f"Esperado: {expected}, Obtenido: {result}")
    
    def test_overlapping_patterns(self):
        """Prueba los algoritmos con patrones solapados."""
        text = "AABAABAAABA"
        pattern = "AABA"
        expected = [0, 3, 7]
        
        for algo_name, algo_func in self.algorithms.items():
            with self.subTest(algorithm=algo_name):
                result = algo_func(text, pattern)
                self.assertEqual(result, expected,
                               f"{algo_name} falló con patrones solapados. "
                               f"Esperado: {expected}, Obtenido: {result}")
    
    def test_no_match(self):
        """Prueba los algoritmos cuando no hay coincidencias."""
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pattern = "12345"
        expected = []
        
        for algo_name, algo_func in self.algorithms.items():
            with self.subTest(algorithm=algo_name):
                result = algo_func(text, pattern)
                self.assertEqual(result, expected,
                               f"{algo_name} falló con patrón sin coincidencias. "
                               f"Esperado: {expected}, Obtenido: {result}")
    
    def test_pattern_longer_than_text(self):
        """Prueba los algoritmos cuando el patrón es más largo que el texto."""
        text = "ABC"
        pattern = "ABCDEF"
        expected = []
        
        for algo_name, algo_func in self.algorithms.items():
            with self.subTest(algorithm=algo_name):
                result = algo_func(text, pattern)
                self.assertEqual(result, expected,
                               f"{algo_name} falló con patrón más largo que el texto. "
                               f"Esperado: {expected}, Obtenido: {result}")

if __name__ == '__main__':
    unittest.main()
