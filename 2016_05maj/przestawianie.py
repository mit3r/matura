


def przestaw(A, n):
    klucz = A[1]
    w = 1

    for k in range(2, n + 1):

        if A[k] < klucz:
            A[w], A[k] = A[k], A[w]
            w += 1

    print('w:', w)

r = []

for d in range(10, 0, -1):
    r += [d+i for i in range(0, 100, 10)]

A = {i+1: v for i, v in enumerate(r)}
n = len(A)
print(n)

print([*A.values()])
przestaw(A, n)
print([*A.values()])

print(A[1], A[2], A[3])


# F F P F


def f(n):

    if n == 1:
        return 4

    else:
        return 1 / (1 - f(n-1))

print(8, f(8))
print(9, f(9))
print(10, f(10))
print(100, f(100))

# F P P F

