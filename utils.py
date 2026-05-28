"""Utilities: Simple arithmetics operations."""


def add(a: int, b: int) -> int:
    """Rturns the sum of two integers.

    Args:
        a: first operand.
        b: second operand.

    Returns:
        Sum of `a` and `b`.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Rturns the difference of two integers.

    Args:
        a: first operand.
        b: second operand.

    Returns:
        Difference of `a` and `b`.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """Rturns the product of two integers.

    Args:
        a: first operand.
        b: second operand.

    Returns:
        Product of `a` and `b`.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """Divides `a` by `b` and returns the result as a float.

    Args:
        a: first operand.
        b: second operand.

    Returns:
        Division of `a` by `b`.

    Raises:
        ValueError: if `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def convert_to_binary(n: int) -> str:
    """Convert a natural number in range 0..100 to its binary representation.

    Args:
        n: integer to convert.

    Returns:
        Binary string without leading '0b'.

    Raises:
        TypeError: if `n` is not an int.
        ValueError: if `n` is outside the range 0..100.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0 or n > 100:
        raise ValueError("Input must be between 0 and 100")
    return bin(n)[2:]
