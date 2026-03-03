import pytest

def check_triangle(side1: int, side2: int, side3: int):
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        result = "Треугольник не существует"
    elif side1 == side2 and side2 == side3 and side1 == side3:
        result = "Равносторонний треугольник"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result

@pytest.mark.parametrize(
    'side1, side2, side3, expected',
    [
        (10, 10, 10, "Равносторонний треугольник"),
        (20, 40, 60, "Треугольник не существует"),
        (5, 5, 3, "Равнобедренный треугольник"),
    ]
)

def test_triangle(side1, side2, side3, expected):
    assert check_triangle(side1, side2, side3) == expected

if __name__ == '__main__':
    pytest.main([__file__, "-v"])