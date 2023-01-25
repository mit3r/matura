if __name__ == '__main__':

    galerie = []
    with open('galerie_przyklad.txt', 'r') as file:

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
    spaces = []
    for kod, miasto, lokale in galerie:
        space = sum([w*h for w, h in lokale])
        spaces += [[miasto, space]]

    print('a)')
    for space in spaces:
        print(*space)

    print('b)')
    print(*max(spaces, key=lambda x: x[1]))
    print(*min(spaces, key=lambda x: x[1]))
    
    print('Zad 4.3')

    miasta_rozne = []
    for kod, miasto, lokale in galerie:

        rozne = {w*h for w, h in lokale}
        miasta_rozne += [[miasto, len(rozne)]]
    
    print(*max(miasta_rozne, key=lambda x: x[1]))
    print(*min(miasta_rozne, key=lambda x: x[1]))