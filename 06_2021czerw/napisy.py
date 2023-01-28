





if __name__ == "__main__":

    napisy  = [ line.strip() for line in open("przyklad.txt") ]

    print(len(napisy[0]))


    cyferki = 0
    for wiersz in napisy:
        for znak in wiersz:

            if ord('0') <= ord(znak) <= ord('9'): 
                cyferki +=1

    print(d)

    print('Zad 4.1', cyferki)

    haslo = [wiersz[i // 20 - 1] for i, wiersz in enumerate(napisy, 1) if i % 20 == 0 ]
    # haslo = [wiersz[i] for i, wiersz in enumerate(wiersze)]
    haslo = "".join(haslo)


    print('Zad 4.2', haslo)

    srodek = ''

    for i, wiersz in enumerate(napisy):

        lewo = wiersz[-1] + wiersz
        if lewo == lewo[::-1]:
            srodek += lewo[25]
            continue

        prawo = wiersz + wiersz[0]
        if prawo == prawo[::-1]:
            srodek += prawo[25]
            continue

    print('Zad 4.3', srodek)

    haslo = ''

    for wiersz in napisy:
        liczby = "".join([z for z in wiersz if '0' <= z <= '9'])

        liczby = [ int(liczby[i : i+2]) for i in range(0, len(liczby), 2) ]
        liczby = [i for i in liczby if 65 <= i <= 90]

        for n in liczby:
            haslo += chr(n)

    isX = 0
    pivot = 0

    for i, znak in enumerate(list(haslo)):
        if znak == 'X':
            isX += 1

            if isX >= 3:
                pivot = i
                break
        


    print('Zad 4.4', "".join(haslo[:pivot+1]))
        

        








