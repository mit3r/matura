def git_para(up, down):

    while True:
        if down < up:
            return False

        if down == up:
            return True

        down //= 2

if __name__ == "__main__":

    pary = [tuple(map(lambda x: int(x), line.strip().split(' ')))
            for line in open('pary.txt', 'r')]

    wyniki = list(filter(lambda para: git_para(*para), pary))


    # short = lambda up, down: False if down < up else True if down == up else short(up, down // 2); [print(*wynik) for wynik in list(filter(lambda para: short(*para), [tuple(map(lambda x: int(x), line.strip().split(' '))) for line in open('pary.txt', 'r')]))]

    [print(*wynik) for wynik in wyniki]
    

