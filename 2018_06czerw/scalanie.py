def zad(p):
    print(f'Zad 4.{p}')

if __name__ == '__main__':

    dane1 = [[*map(int, line.strip().split(' '))] for line in open('dane1.txt')]
    dane2 = [[*map(int, line.strip().split(' '))] for line in open('dane2.txt')]

    zad(1)
    odp = 0
    for c1, c2 in zip(dane1, dane2):
        if c1[-1] == c2[-1]:
            odp += 1

    print(odp)

    zad(2)
    odp = 0
    for c1, c2 in zip(dane1, dane2):
        
        even1 = len([n for n in c1 if n % 2 == 0])
        odd1 = len([n for n in c1 if n % 2 == 1])

        even2 = len([n for n in c2 if n % 2 == 0])
        odd2 = len([n for n in c2 if n % 2 == 1])

        if even1 == odd1 == even2 == odd2 == 5:
            odp += 1
    
    print(odp)

    zad(3)
    odp = []

    for i, v in enumerate(zip(dane1, dane2)):
        c1, c2 = v

        if set(c1) == set(c2):
            odp += [i+1]
    
    print('ile:', len(odp), 'wiersze: ', *odp)

    zad(4)
    for c1, c2 in zip(dane1, dane2):
        c3 = []
        pivot1 = 0
        pivot2 = 0
        
        while pivot1 < len(c1) and pivot2 < len(c2):

            if c1[pivot1] < c2[pivot2]:
                c3 += [c1[pivot1]]
                pivot1 += 1
            else:
                c3 += [c2[pivot2]]
                pivot2 += 1

        if(len(c1[pivot1:])) != 0:
            print(*c3, *c1[pivot1:])
        else:
            print(*c3, *c2[pivot2:])