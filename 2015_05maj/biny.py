
z = lambda n: print(f'Zad. {n}')

liczby = [line.strip() for line in open('liczby.txt')]

z(1)

odp = 0

for n in liczby:
    zera = n.count('0')
    jedyn = n.count('1')

    if zera > jedyn:
        odp += 1

print(odp)


z(2)

div8 = 0
div2 = 0


for n in liczby:

    if n[-1] == '0': 
        div2 += 1

    if n[-3: ] == '000':
        div8 += 1

print(f'przez 2: {div2}, przez 8: {div8}')

z(3)

long = len(max(liczby, key=lambda x: len(x)))

longests = [ n for n in liczby if len(n) == long]

i = 0

while len(longests) > 1:

    if any([n[i] == '1' for n in longests]):
        longests = [n for n in longests if n[i] == '1']
    
    i += 1

print('max', liczby.index(*longests)+1)

short = len(min(liczby, key=lambda x: len(x)))

shortests = [ n for n in liczby if len(n) == short]
i = 0

while len(shortests) > 1:

    if any([n[i] == '0' for n in shortests]):
        shortests = [n for n in shortests if n[i] == '0']
    
    i += 1

print('min', liczby.index(*shortests)+1)
         
