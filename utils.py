"""Utilities: proste operacje arytmetyczne."""


def add(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych.

    Args:
        a: pierwszy składnik.
        b: drugi składnik.

    Returns:
        Suma `a + b`.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Zwraca różnicę `a - b`."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Zwraca iloczyn `a * b`."""
    return a * b


def divide(a: int, b: int) -> float:
    """Dzieli `a` przez `b` i zwraca wynik jako float.

    Raises:
        ValueError: jeśli `b` jest równe zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
