"""
GRAFY NIESKIEROWANE
"""

# graf spojny, ktory ma dwa cykle 0-1-2-0 i 3-4-5-3
G1 = [
    [1, 2],    # 0
    [0, 2],    # 1
    [0, 1, 3], # 2 — cykl: 0–1–2–0
    [2, 4, 5], # 3
    [3, 5],    # 4
    [3, 4]     # 5 — cykl: 3–4–5–3
]

# graf spojny który ma jeden cykl 1-2-3-4-1; cykl czterech wierzchołków
G2 = [
    [1],       # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [2, 4],    # 3
    [3, 1]     # 4 — cykl: 1–2–3–4–1
]

# graf spojny bez cyklu
G3 = [
    [1],       # 0
    [0, 2],    # 1
    [1, 4],       # 2
    [4],       # 3
    [2, 3]        # 4
]

# graf spojny z jednym cyklem czterech wierzchołków
G4 = [
    [1, 3],    # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [0, 2],    # 3 — cykl: 0–1–2–3–0
    [1, 5],    # 4
    [4]        # 5
]

# niespojny graf, z dwoma spojnymi skladowymi
G5 = [
    [1],  # 0 ┐
    [0, 2],  # 1 ┼─ spójna składowa A: 0–1–2
    [1],  # 2 ┘

    [4, 5],  # 3 ┐
    [3, 5],  # 4 ┼─ spójna składowa B: 3–4–5 (trójkąt)
    [3, 4]  # 5 ┘
]

# niespojny graf z czterema spojnymi skladowymi
G6 = [
    [1],       # 0 ┐
    [0],       # 1 ┘   — komponent A: 0–1

    [3],       # 2 ┐
    [2],       # 3 ┘   — komponent B: 2–3

    [],        # 4     — komponent C: samotny wierzchołek

    [6, 7],    # 5 ┐
    [5, 7],    # 6 ┼─   — komponent D: 5–6–7 (trójkąt)
    [5, 6]     # 7 ┘
]

"""
GRAFY WAŻONE
"""

g1= [
    [(1, 3), (2, 5)],       # wierzchołek 0 połączony z 1 (waga 3) i 2 (waga 5)
    [(0, 3), (2, 1), (3, 4)], # wierzchołek 1 połączony z 0, 2, 3
    [(0, 5), (1, 1), (4, 7)], # wierzchołek 2 połączony z 0, 1, 4
    [(1, 4), (4, 2)],       # wierzchołek 3 połączony z 1, 4
    [(2, 7), (3, 2)]        # wierzchołek 4 połączony z 2, 3
]

g1_matrix = [
#  0    1    2    3    4
  [ 0,  3,  5, -1, -1],  # 0
  [ 3,  0,  1,  4, -1],  # 1
  [ 5,  1,  0, -1,  7],  # 2
  [-1,  4, -1,  0,  2],  # 3
  [-1, -1,  7,  2,  0]   # 4
]
