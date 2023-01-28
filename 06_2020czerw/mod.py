# F P F P

n = 11_111

print(sum([int(i) for i in str(n)]))

w = 0
while n != 0:
    w += (n % 10)
    print('w', w)
    n = n // 10

print(w)