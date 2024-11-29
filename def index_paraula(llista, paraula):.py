def index_paraula(llista, paraula):
    """Retorna l'índex de la paraula en la llista, o -1 si no es troba."""
    for index, p in enumerate(llista):
        if p == paraula:
            return index
    return -1

# Proves de la funció
llista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(index_paraula(llista, 'c'))  # Retorna 2
print(index_paraula(llista, 'a'))  # Retorna 0
print(index_paraula(llista, 'g'))  # Retorna 6
print(index_paraula(llista, 'z'))  # Retorna -1
print(index_paraula([], 'a'))       # Retorna -1