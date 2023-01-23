
class szach:

    def print(plansza):
        for wiersz in plansza:
            print(wiersz)

    def wiersz(plansza, w):
        return plansza[w]

    def kolumna(plansza, k):
        return ''.join([wiersz[k] for wiersz in plansza])


def czy_szachuje(wieza, krol, wiersz: str):

    krol = wiersz.find(krol)
    wieza = wiersz.find(wieza)
    miedzy = wiersz[krol+1:wieza]

    return krol != -1 and wieza != -1 and len(miedzy) == miedzy.count('.')


if __name__ == "__main__":
    with open('szachy.txt') as file:

        plansze = [plansza.split() for plansza in file.read().split('\n\n')]

    boardSize = len(plansze[0][0])

    piony_czarne = 'k w s h g p'.split()
    piony_biale = [p.upper() for p in piony_czarne]

    atLeastOneEmpty = 0
    maxEmptyCols = 0
    for plansza in plansze:

        tempEmptyCols = 0
        temp_emptiness = False
        for k in range(boardSize):

            if szach.kolumna(plansza, k) == '.'*8:
                tempEmptyCols += 1
                temp_emptiness = True

        if tempEmptyCols > maxEmptyCols:
            maxEmptyCols = tempEmptyCols

        if temp_emptiness:
            atLeastOneEmpty += 1

    print('Zad. 1.1', atLeastOneEmpty, maxEmptyCols)

    rownowagi = 0
    minimum_sum = boardSize**2

    for plansza in plansze:

        white_count = {i: 0 for i in piony_biale}  # DUZE
        black_count = {i: 0 for i in piony_czarne}  # male

        for wiersz in plansza:
            for bierka in wiersz:
                if bierka == '.':
                    continue

                if 'A' <= bierka <= 'Z':
                    white_count[bierka] += 1
                    continue

                if 'a' <= bierka <= 'z':
                    black_count[bierka] += 1
                    continue

        to_samo = [
            white_count[rodzaj.upper()] == black_count[rodzaj]
            for rodzaj in piony_czarne
        ]

        ilosc_razem = sum(list(white_count.values())) * 2
        if not False in to_samo and ilosc_razem:
            
            rownowagi += 1
            
            if ilosc_razem < minimum_sum:
                minimum_sum = ilosc_razem

    print('Zad. 1.2', rownowagi, minimum_sum)

    biala_szach = 0
    czarna_szach = 0
    for plansza in plansze:

        for wiersz in plansza:

            if czy_szachuje('w', 'K', wiersz):
                czarna_szach += 1

            if czy_szachuje('W', 'k', wiersz):
                biala_szach += 1

        for k in range(boardSize):

            kolumna = szach.kolumna(plansza, k)
            if czy_szachuje('w', 'K', kolumna):
                czarna_szach += 1

            if czy_szachuje('W', 'k', kolumna):
                biala_szach += 1

print('Zad 1.3', biala_szach, czarna_szach)
