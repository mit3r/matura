

def koduj(tab: str, k):

    ilosc = abs(65 - 90) + 1

    alfa = {chr(znak): chr(((znak+ k - 65) % ilosc)+65) for znak in range(65, 90+1)}

    return "".join([alfa[znak] for znak in tab])


# print(koduj('INTERPRETOWANIE', 107))
# print(koduj('LQWHUSUHWRZDQLH', 26 - 107 % 26 ))


dane = [line.strip().split() for line in open('dane_6_3.txt', 'r')]

for tekst, szyfr in dane:

    if tekst not in [koduj(szyfr, i) for i in range(0, 26+1)]:
        print(tekst)