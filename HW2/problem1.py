import math


def calculate_distance(x1, y1, x2, y2):
    """
    Calcu
    Args:
      x1: X for input location 1 
      x2: Y for input location 1
      y1: X for input location 2
      y2: Y for input location 2

    Returns:
      The Euclidean distance
    """
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)


if __name__ == "__main__":
    print(calculate_distance(x1=2, y1=1, x2=3, y2=2))
