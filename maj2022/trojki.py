


if __name__ == "__main__":

    liczby = [line.strip() for line in open('liczby.txt', 'r')]

    takie_same = list(filter(lambda x: x[0] == x[-1], liczby))

    # same = [x for x in liczby if x[0] == x[-1]]
    # print(same)
    # juz lambdy jest łatwiej pojąć

    print('Zad 4.1', len(takie_same), takie_same[0])

    czynniki = {liczba: [] for liczba in liczby}

    for liczba in czynniki.keys():
        n = int(liczba)
        i = 2
        while n > 1 and i != int(liczba):

            if n % i == 0:
                n //= i
                czynniki[liczba].append(i)
                i = 2
                continue
            i += 1

    most_factors_quantity = 0
    most_factors_number = 0

    for rozklad in czynniki.keys():
        if len(czynniki[rozklad]) > most_factors_quantity:
            most_factors_quantity = len(czynniki[rozklad])
            most_factors_number = rozklad

    diff_factors_quantity = 0
    diff_factors_number = 0

    for rozklad in czynniki.keys():
        uniques = set(czynniki[rozklad])

        if len(uniques) > diff_factors_quantity:
            diff_factors_quantity = len(uniques)
            diff_factors_number = rozklad

    print(
        'Zad 4.2',
        most_factors_number,
        most_factors_quantity,
        diff_factors_number,
        diff_factors_quantity
    )

    liczby = [int(liczba) for liczba in liczby]

    maksimum = max(liczby)
    minimum = min(liczby)

    trojki = set()
    piatki = set()

    for liczba in liczby:

        krotnosci = [n for n in liczby if n % liczba == 0]

        if len(krotnosci) < 2:
            continue       
        
        krotnosci.sort()

        for i1 in krotnosci:
            for i2 in krotnosci:
                for i3 in krotnosci:
                    
                    if i3 % i2 == 0 and i2 % i1 == 0 and i1 != i2 != i3 :
                        trojki.add(tuple(map( lambda x: str(x), (i1, i2, i3))))

                    for i4 in krotnosci:
                        for i5 in krotnosci:

                            if i5 % i4 == 0 and i4 % i3 == 0 and i3 % i2 == 0 and i2 % i1 == 0 and i1 != i2 != i3 != i4 != i5 :
                                piatki.add(tuple(map( lambda x: str(x), (i1, i2, i3, i4, i5))))



    print('Trojki')
    for t in trojki:
        print(" ".join(list(t)))

    print(len(trojki))

    print('Piatki')
    for p in piatki:
        print(" ".join(list(p)))
    
    print(len(piatki))
        
                    





        #     for pivot in range(1, len(krotnosci) - step*2 ):

        #         if (krotnosci[pivot+2*step]*liczba % krotnosci[pivot+step]*liczba == 0 
        #         and krotnosci[pivot+step]*liczba % krotnosci[pivot]*liczba == 0):

        #             trojki.add((
        #                 krotnosci[pivot]*liczba,
        #                 krotnosci[pivot+step]*liczba,
        #                 krotnosci[pivot+2*step]*liczba,
        #             ))

    # print(trojki)
