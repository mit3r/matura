

# 1
# n + 1 - i

#REG(x, m)


def reg(w):
    if len(w) == 1:
        return 1

    if w != w[::-1]:
        return 0

    w1 = w[:len(w) // 2]
    return reg(w1) + 1

dane = [
    'BABBAB',
    'BABBBB',
    'BAAAAB',
    'B',
    'BBB',
    'AAAAAAAA',
]

for w in dane:
    print(w, reg(w))