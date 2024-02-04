from itertools import permutations

t = int(input())

while t:
    n = int(input())

    target = (14 ** (n//2)) ** 2

    for i in permutations(list(str(target))):
        x = int("".join(i))
        if x**0.5 == int(x**0.5):
            print(x)

    t -= 1