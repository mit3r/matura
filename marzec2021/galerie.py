if __name__ == '__main__':

    galerie = []
    with open('galerie.txt', 'r') as file:

        for line in file:
            kod, miasto, *pary = line.strip().split(' ')

            even = pary[::2]
            odd = pary[1::2]

            lokale = list(zip(even, odd))
            lokale = [(int(w), int(h)) for w, h in lokale if int(w) and int(h)]

            galerie += [[kod, miasto, lokale]]

    kraje = {miasto: 0 for miasto, *reszta in galerie}

    kody = [kod for kod, *reszta in galerie]

    for key in kraje.keys():
        kraje[key] = kody.count(key)

    print('Zad. 4.1')
    print(kraje)

    print('Zad. 4.2')
    print('a)')

    maks_space = 0
    maks_space_name = ''

    min_space = 1000000
    min_space_name = ''

    for kod, miasto, lokale in galerie:

        space = sum([w*h for w, h in lokale])

        print(miasto, space, len(lokale))

        if space > maks_space:
            maks_space = space
            maks_space_name = miasto
        
        if space < min_space:
            min_space = space
            min_space_name = miasto

    print('b)')

    print(maks_space_name, maks_space)
    print(min_space_name, min_space)

    print('Zad 4.3')

    miasta_rozne = []
    for kod, miasto, lokale in galerie:

        rozne = {w*h for w, h in lokale}
        miasta_rozne += [[miasto, len(rozne)]]
    
    min_roz = 100000
    min_roz_name = ''

    maks_roz = 0
    maks_roz_name = ''

    for miasto, ilosc in miasta_rozne:

        if ilosc < min_roz:
            min_roz = ilosc
            min_roz_name = miasto

        if ilosc > maks_roz:
            maks_roz = ilosc
            maks_roz_name = miasto
    
    print(maks_roz_name, maks_roz)
    print(min_roz_name, min_roz)