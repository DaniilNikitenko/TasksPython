# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

# Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:


def perimeter(n):
    seq = []
    a, b = 0, 1
    for _ in range(n + 2):
        seq.append(a)
        a, b = b, a + b
    return 4 * sum(seq)
