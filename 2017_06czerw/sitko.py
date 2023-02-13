import math

def Sitko(n):
    global Czyjest, j, count

    for i in range(1, n+1):
        Czyjest[i] = False

    j = 1

    while j*j < n:
        j = j + 1

    for i in range(2, j+1):
        kw = i * i
        poz = kw
        while poz <= n:
            Czyjest[poz] = True

            count += 1
            poz = poz + kw


def Sitko_mod(n, d):
    global Czyjest, j, count

    for i in range(1, n+1):
        Czyjest[i] = False

    for i in range(2, j+1):
        kw = i * i
        poz = kw
        while poz <= n:
            Czyjest[poz] = True
            if i == d:
                count +=  1
            poz = poz + kw

count = 0
for n, k in [
    [10, 9],
    [10, 5],
    [100, 10],
    [100, 75],
]:
    j = 1
    Czyjest = {i+1: None for i in range(n+1)}

    Sitko(n)

    print('Czyjest[k]', Czyjest[k])
    print('j', j)

print('kolejne')


for u in [2, 3, 5, 9]:
    n = 100
    Czyjest = {i+1: None for i in range(n+1)}
    count = 0
    Sitko_mod(100, u)

    print(count)


count = 0
n= 100
Czyjest = {i+1: None for i in range(n+1)}
Sitko(n)


print('Ma być większe od', count)

print(math.log(100))
print(100)

w = 0
for i in range(2, 10+1):

    w += 1 / (2**i)

    print(1 / (2**i))



print(w*100)
print(100**(1/2))

# F P F F


