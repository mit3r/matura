

initial = {i: None for i in range(1, 11)}

S, P = initial.copy(), initial.copy()

n = 10

for i in range(1, n+1):
    P[i] = 1
    S[i] = 0

for j in range(2, n+1):
    if P[j] == 1:
        i = j * j

        while i <= n:
            P[i] = 0
            i = i + j

    S[j] = S[j-1] + P[j]

for key, val in S.items():
    print(f'S[{key}] =', val)

a = 3
b = 7
# Odp B

print(S[b] - S[a - 1])