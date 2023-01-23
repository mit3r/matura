

def abslowo(n: int, s: str):

    s = ' ' + s
    A = [0]

    for i in range(1, n+1):
        if s[i] == 'a':
            A.append(A[i-1] + 1)
        else:
            A.append(A[i-1])

    B = [0 for i in range(n+2)]

    for j in range(n, 0, -1):
        if s[j] == 'b':
            B[j] = B[j+1] + 1
        else:
            B[j] = B[j + 1]

    k = 1

    for i in range(n+1):
        if A[i] + B[i+1] > k:
            k = A[i] + B[i+1]

    return k


if __name__ == '__main__':

    dane = [
        [5, 'aabab'],
        [2, 'ab'],
        [3, 'aaa'],
        [6, 'aababb'],
        [9, 'baabbaaab'],
    ]

    for d in dane:
        print(d[0], d[1], abslowo(d[0], d[1]))

    s = ['a']*300 + ['b'] * 550 + ['a'] * 300 + ['b']*7 + ['a']*280 + ['b'] * 110
    s = "".join(s)
    print(s)
    print(1, abslowo(1, s))
            