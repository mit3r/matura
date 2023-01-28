


if __name__ == "__main__":

    tekst = [line.split() for line in open('./maj2021/przyklad.txt', 'r')]

    litery = set([komenda[1] for komenda in tekst])
    ilosc = {litera: 0 for litera in litery}

    for komenda in tekst:
        ilosc[komenda[1]] += 1

    print(ilosc)


