neighbors = {
    'q': {'w', 'a', 's'},
    'w': {'q', 'e', 'a', 's', 'd'},
    'e': {'w', 'r', 's', 'd', 'f'},
    'r': {'e', 't', 'd', 'f', 'g'},
    't': {'r', 'y', 'f', 'g', 'h'},
    'y': {'t', 'u', 'g', 'h', 'j'},
    'u': {'y', 'i', 'h', 'j', 'k'},
    'o': {'i', 'p', 'k', 'l'},
    'a': {'q', 'w', 's', 'z', 'x'},
    's': {'q', 'w', 'e', 'a', 'd', 'z', 'x', 'c'},
    'd': {'w', 'e', 'r', 's', 'f', 'x', 'c', 'v'},
    'f': {'e', 'r', 't', 'd', 'g', 'c', 'v', 'b'},
    'g': {'r', 't', 'y', 'f', 'h', 'v', 'b', 'n'},
    'h': {'t', 'y', 'u', 'g', 'j', 'b', 'n', 'm'},
    'j': {'y', 'u', 'i', 'h', 'k', 'n', 'm'},
    'k': {'u', 'i', 'o', 'j', 'l', 'm'},
    'l': {'i', 'o', 'p', 'k'},
    'z': {'a', 's', 'x'},
    'x': {'a', 's', 'd', 'z', 'c'},
    'c': {'s', 'd', 'f', 'x', 'v'},
    'v': {'d', 'f', 'g', 'c', 'b'},
    'b': {'f', 'g', 'h', 'v', 'n'},
    'n': {'g', 'h', 'j', 'b', 'm'},
    'm': {'h', 'j', 'k', 'n'}
}

def getNeighbors(c):
    if c in neighbors:
        return neighbors[c]
    else:
        return set()