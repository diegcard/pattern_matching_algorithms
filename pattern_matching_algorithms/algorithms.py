"""
Módulo con implementaciones de diferentes algoritmos de pattern matching.
"""

from typing import List, Dict

def brute_force(text: str, pattern: str) -> List[int]:
    """
    Implementación del algoritmo de fuerza bruta para pattern matching.
    
    Args:
        text: El texto en el que buscar
        pattern: El patrón a buscar
        
    Returns:
        Lista de posiciones donde el patrón aparece en el texto
    """
    if not pattern:
        return []
    
    n = len(text)
    m = len(pattern)
    positions = []
    
    # Recorre el texto hasta donde sea posible encontrar el patrón completo
    for i in range(n - m + 1):
        j = 0
        # Compara cada carácter del patrón con el texto
        while j < m and text[i + j] == pattern[j]:
            j += 1
        # Si j alcanzó el final del patrón, entonces hubo una coincidencia
        if j == m:
            positions.append(i)
    
    return positions

def knuth_morris_pratt(text: str, pattern: str) -> List[int]:
    """
    Implementación del algoritmo Knuth-Morris-Pratt para pattern matching.
    
    Args:
        text: El texto en el que buscar
        pattern: El patrón a buscar
        
    Returns:
        Lista de posiciones donde el patrón aparece en el texto
    """
    if not pattern:
        return []
    
    # Construye la tabla de fallos (tabla de prefijos y sufijos)
    def build_failure_table(pattern: str) -> List[int]:
        m = len(pattern)
        failure = [0] * m
        j = 0
        
        for i in range(1, m):
            # Si hay un desajuste, retrocede usando la tabla de fallos
            while j > 0 and pattern[j] != pattern[i]:
                j = failure[j - 1]
            
            # Si hay una coincidencia, avanza en el patrón
            if pattern[j] == pattern[i]:
                j += 1
            
            failure[i] = j
        
        return failure
    
    n = len(text)
    m = len(pattern)
    positions = []
    
    # Si el patrón es más largo que el texto, no puede haber coincidencias
    if m > n:
        return positions
    
    # Construye la tabla de fallos para el patrón
    failure = build_failure_table(pattern)
    
    # Algoritmo KMP principal
    j = 0  # Posición actual en el patrón
    for i in range(n):
        # Si hay un desajuste, retrocede usando la tabla de fallos
        while j > 0 and pattern[j] != text[i]:
            j = failure[j - 1]
        
        # Si hay una coincidencia, avanza en el patrón
        if pattern[j] == text[i]:
            j += 1
        
        # Si hemos llegado al final del patrón, hemos encontrado una coincidencia
        if j == m:
            positions.append(i - m + 1)
            # Retrocede para encontrar solapamientos
            j = failure[j - 1]
    
    return positions

def boyer_moore(text: str, pattern: str) -> List[int]:
    """
    Implementación del algoritmo Boyer-Moore para pattern matching.
    
    Args:
        text: El texto en el que buscar
        pattern: El patrón a buscar
        
    Returns:
        Lista de posiciones donde el patrón aparece en el texto
    """
    if not pattern:
        return []
    
    n = len(text)
    m = len(pattern)
    positions = []
    
    # Si el patrón es más largo que el texto, no puede haber coincidencias
    if m > n:
        return positions
    
    # Regla del carácter malo (Bad Character Rule)
    # Para cada carácter, guarda la posición de su última aparición en el patrón
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    # Algoritmo principal de Boyer-Moore
    s = 0  # s es el desplazamiento del patrón con respecto al texto
    while s <= n - m:
        j = m - 1  # Empezar a comparar desde el final del patrón
        
        # Comparar caracteres del patrón con el texto de derecha a izquierda
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # Si j es -1, significa que hemos encontrado una coincidencia
        if j < 0:
            positions.append(s)
            # Mover el patrón para buscar la siguiente ocurrencia
            s += 1
        else:
            # Calcular el desplazamiento usando la regla del carácter malo
            # Si el carácter que causó el desajuste no está en el patrón, 
            # mover todo el patrón
            # Si está en el patrón, alinear con su última aparición
            char = text[s + j]
            if char in bad_char:
                # Mover para alinear el patrón con el carácter en el texto
                s += max(1, j - bad_char[char])
            else:
                # El carácter no está en el patrón, mover todo el patrón
                s += j + 1
    
    return positions

def rabin_karp(text: str, pattern: str, q: int = 101) -> List[int]:
    """
    Implementación del algoritmo Rabin-Karp para pattern matching.
    
    Args:
        text: El texto en el que buscar
        pattern: El patrón a buscar
        q: Un número primo para el hashing
        
    Returns:
        Lista de posiciones donde el patrón aparece en el texto
    """
    if not pattern:
        return []
    
    n = len(text)
    m = len(pattern)
    positions = []
    
    # Si el patrón es más largo que el texto, no puede haber coincidencias
    if m > n:
        return positions
    
    # Valor de la potencia d^(m-1) donde d es el tamaño del alfabeto
    d = 256  # Asumimos ASCII
    h = pow(d, m - 1) % q
    
    p = 0  # Hash del patrón
    t = 0  # Hash de la ventana actual en el texto
    
    # Calcular el hash inicial del patrón y la primera ventana del texto
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    # Deslizar la ventana sobre el texto
    for i in range(n - m + 1):
        # Si los hashes coinciden, verificar caracteres uno por uno
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            
            if match:
                positions.append(i)
        
        # Calcular el hash para la siguiente ventana
        if i < n - m:
            # Restar el dígito que sale, agregar el que entra
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            
            # Asegurarse de que t sea no-negativo
            if t < 0:
                t += q
    
    return positions

def aho_corasick(text: str, pattern: str) -> List[int]:
    """
    Implementación simplificada del algoritmo Aho-Corasick.
    
    Nota: Esta es una implementación básica para un solo patrón.
    El algoritmo Aho-Corasick es más eficiente para buscar múltiples patrones.
    
    Args:
        text: El texto en el que buscar
        pattern: El patrón a buscar
        
    Returns:
        Lista de posiciones donde el patrón aparece en el texto
    """
    # Para un solo patrón, usamos KMP como implementación simplificada
    # En una implementación real de Aho-Corasick, construiríamos un autómata
    # que pueda buscar múltiples patrones simultáneamente
    return knuth_morris_pratt(text, pattern)

# Implementación real de Aho-Corasick para múltiples patrones
def aho_corasick_multiple(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Implementación del algoritmo Aho-Corasick para múltiples patrones.
    
    Args:
        text: El texto en el que buscar
        patterns: Lista de patrones a buscar
        
    Returns:
        Diccionario con patrones como claves y listas de posiciones como valores
    """
    # Implementación de un nodo del trie
    class Node:
        def __init__(self):
            self.goto = {}  # Transiciones del autómata
            self.out = []   # Patrones que terminan en este nodo
            self.fail = None  # Enlace de fallo
    
    # Construir el trie para los patrones
    def build_trie(patterns: List[str]) -> Node:
        root = Node()
        
        # Agregar cada patrón al trie
        for i, pattern in enumerate(patterns):
            node = root
            for char in pattern:
                if char not in node.goto:
                    node.goto[char] = Node()
                node = node.goto[char]
            node.out.append(i)  # Guardar el índice del patrón
        
        return root
    
    # Construir enlaces de fallo usando BFS
    def build_failure_links(root: Node) -> None:
        queue = []
        
        # Para los hijos de la raíz, el enlace de fallo es la raíz
        for char, child in root.goto.items():
            child.fail = root
            queue.append(child)
        
        # BFS para construir enlaces de fallo para el resto del trie
        while queue:
            node = queue.pop(0)
            
            for char, child in node.goto.items():
                queue.append(child)
                
                # Encontrar el enlace de fallo para este nodo
                fail = node.fail
                while fail and char not in fail.goto:
                    fail = fail.fail
                
                child.fail = fail.goto[char] if fail and char in fail.goto else root
                
                # Agregar salidas del nodo de fallo a este nodo
                if child.fail:
                    child.out.extend(child.fail.out)
    
    # Búsqueda de patrones en el texto usando el autómata
    def search(text: str, root: Node, patterns: List[str]) -> Dict[str, List[int]]:
        results = {pattern: [] for pattern in patterns}
        node = root
        
        for i, char in enumerate(text):
            # Seguir los enlaces de fallo hasta encontrar un nodo con transición
            while node is not root and char not in node.goto:
                node = node.fail
            
            # Si hay una transición para este carácter, seguirla
            if char in node.goto:
                node = node.goto[char]
            
            # Verificar las salidas (patrones encontrados) en este nodo
            for pattern_idx in node.out:
                pattern = patterns[pattern_idx]
                start_pos = i - len(pattern) + 1
                results[pattern].append(start_pos)
        
        return results
    
    # Implementar el algoritmo completo
    if not patterns:
        return {}
    
    # Construir el autómata
    root = build_trie(patterns)
    build_failure_links(root)
    
    # Buscar patrones en el texto
    results = search(text, root, patterns)
    
    # Si solo se proporcionó un patrón, simplificar la salida
    if len(patterns) == 1 and pattern in patterns:
        return {pattern: results[pattern]}
    
    return results
