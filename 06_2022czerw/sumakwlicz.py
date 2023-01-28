

def SumaKwCyfr(n): 

    suma = 0

    while n > 0:
        cyfra = n % 10
        n //= 10

        suma += cyfra * cyfra

    return suma


def CzyNudna(n):


    ciag = [SumaKwCyfr(n)]
    while True:

        if ciag[-1] == 1:
            return True

        nowy = SumaKwCyfr(ciag[-1])

        if ciag.__contains__(nowy):
            return False

        ciag.append(nowy)

if __name__ == "__main__":

    for n in [13, 4, 229, 82]:
        print(n, CzyNudna(n))