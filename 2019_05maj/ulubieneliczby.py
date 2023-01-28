

def start_parzyste(n, A):

    left = 1
    right = n

    while left < right:
        i = (left + right) // 2

        if A[i] % 2 != 0:
            left = i + 1
        else:
            right = i

        i = left + right // 2

    return A[right]


A = {i+1: v for i, v in enumerate([5, 99, 3, 7, 111, 13, 4, 24, 4, 8])}
w = start_parzyste(len(A), A)

print(w)
