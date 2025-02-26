# fichier rectangle.py
def area_rectangle(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Les entrées doivent être des nombres.")
    if length <= 0 or width <= 0:
        raise ValueError("Les dimensions doivent être positives.")
    return length * width