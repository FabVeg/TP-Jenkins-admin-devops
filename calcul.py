# fichier multiplication.py
def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Les entrées doivent être des nombres.")
    return a * b