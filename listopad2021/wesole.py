

def czy_wesola(n):

    wyst = []
    i = n
    while True:

        i = sum([int(cyfra)**2 for cyfra in str(i)])

        if i in wyst or i == n:
            return False
        
        if i == 1:
            return True

        wyst.append(i)

def podaj_wesole(n):

    wyst = []
    i = n
    print('n wynosi', n)

    while True:

        i = sum([int(cyfra)**2 for cyfra in str(i)])
        print(i)

        if i in wyst or i == n:
            return []
        
        if i == 1:
            return [n] + wyst + [1]

        wyst.append(i)

max_count = 0
for i in range(1, 1000+1):

    w = podaj_wesole(i)

    # print(w)

    if len(w) > max_count:
        max_count = len(w)


wypisane = []
for i in range(1, 1000+1):

    w = podaj_wesole(i)

    if len(w) == max_count:
        wypisane += w

wypisane = list(set(wypisane))
wypisane.sort()
wypisane = wypisane[-1::-1]

print('Zad 4.1')
print(max_count)
print(" ".join([str(i) for i in wypisane if czy_wesola(i)]))


# i koniec XD


        