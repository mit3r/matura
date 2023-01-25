
def suma_cyfr(n: str):
    return sum([int(i) for i in n])

def isPal(n: str):
    return n == n[-1::-1]

if __name__ == '__main__':
    path = 'identyfikator.txt'
    ids = [line.strip() for line in open(path, 'r')]
    ids = [(line[:3], line[3:]) for line in ids]
    
    sumy = [(seria + numer, suma_cyfr(numer)) for seria, numer in ids]

    maximum = max(sumy, key=lambda x: x[1])[1]

    najwyzsze = [id for id, suma in sumy if suma == maximum]

    print('Zad 4.1', najwyzsze)

    print('Zad 4.2')
    for seria, numer in ids:
        if isPal(seria) or isPal(numer):
            print(seria+numer)

    szyfr = {chr(i).upper(): i-97+10 for i in range(ord('a'), ord('z') + 1)}

    print('Zad 4.3')
    for seria, numer in ids:
        kontrol = int(numer[0])

        a = [int(szyfr[znak]) for znak in seria]
        b = [int(i) for i in numer[1:]]

        suma = sum([i*w for i, w in zip(a+b, [7,3,1, 7,3,1 ,7,3])])

        if suma % 10 != kontrol:
            print(seria+numer)