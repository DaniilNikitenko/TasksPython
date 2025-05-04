# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:


def tower_builder(n_floors):
    n_list = []
    num = 1
    for _ in range(n_floors):
        n_list.append("*" * num)
        num += 2
    max_len = len(n_list[-1])
    return [s.center(max_len) for s in n_list]


print(tower_builder(4))
