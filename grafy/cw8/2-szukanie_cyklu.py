"""
Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
graf reprezentowany jest przez macierz sasiedztwa A.
"""
def find4cycle(G):
    n = len(G)