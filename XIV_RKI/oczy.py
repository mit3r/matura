import time


def slownikuj(wyniki: str):
    # /mo-1/rt-0.05/ph-6.5/ar-0.25/bzt-750/ddt-0/pcb-0/fo-10/bo-5/ch-500/
    wyniki = [wynik.split('-') for wynik in wyniki.split('/')[1:-1]]
    wyniki = {sym: float(wart) for sym, wart in wyniki}
    return wyniki


if __name__ == '__main__':

    normy = [line.strip().split() for line in open('normy.txt', 'r')]
    normy = {key: a for key, *a in normy}
    normy = {key: [*map(float, value)] for key, value in normy.items()}

    dane = [line.strip().split() for line in open('dane.txt', 'r')][:10]
    dane = [{
        'loc': int(loc),
        'data': data,
        'godz': godz,
        'wynik': slownikuj(wyniki),
    } for loc, data, godz, wyniki in dane]

    repeat, good, bad = [], [], []

    for krotka in dane:
        loc, data, godz, wyniki = krotka.values()

        # czy parametry istnieją w spisie norm
        if any([param not in normy.keys() for param in wyniki.keys()]):
            repeat += [loc]
            continue

        # czy parametry spełniają normy
        for param, value in wyniki.items():

            if len(normy[param]) == 2:
                maks, mini = max(normy[param]), min(normy[param])
                if not (maks >= value >= mini):
                    bad += [loc]
                    break

            else:
                if value != normy[param][0]:
                    bad += [loc]
                    break

        else:
            good += [loc]

    print('repeat', repeat)
    print('good', good)
    print('bad', bad)

    with open('wyniki_zad3.txt', 'w') as file:
        file.write(
            f"""
Liczba próbek do ponownej analizy wynosi: {len(repeat)}
Liczba próbek nie spełniających normy wynosi:  {len(bad)}
Liczba próbek spełniających normy wynosi: {len(good)}
"""
        )

    dane = [ line.strip() for line in open('dane.txt', 'r')]
    dane = {int(line.split()[0]): line for line in dane}

    tasks = [
        ['ponowna_analiza.txt', repeat],
        ['spelnia_normy.txt', good],
        ['nie_spelnia_norm.txt', bad],
    ]

    for path, list in tasks:
        with open(path, 'w') as file:
            for loc in list:
                file.write(f'{dane[loc]}\n')