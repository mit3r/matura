

if __name__ == "__main__":

    # piksele = []
    # with open('dane.txt', 'r') as file:
    #     for line in file:
    #         piksele.append(list(map(lambda x: int(x), line.split())))

    piksele = [[int(x) for x in line.split()] for line in open('przyklad.txt', 'r')]

    bright = 0
    dark = 255

    d = [1, 8, 40, -5, 13, 0, 5, 2]
    
    extremes = lambda lista, maks='', min='': (extremes(lista, lista[0], lista[0]) if maks == '' and min ==''else extremes(lista[1:], lista[0] if lista[0] > maks else maks, lista[0] if lista[0] < min else min)) if len(lista) else (maks, min)

    print(extremes(d))

    maks = 0

    for row in piksele:
        for jasnosc in row:
            if jasnosc > bright:
                bright = jasnosc

            if jasnosc < dark:
                dark = jasnosc

    print('6.1.', 'darkest:', dark, 'brightest:', bright)

    odpady = 0
    for row in piksele:
        r = len(row)-1
        l = 0
        while l + 1 != r:
            if row[l] != row[r]:
                odpady += 1
                break

            r -= 1
            l += 1

        # chad bot big head

        # if row[:160] != row[160:][::-1]:
        #     odpady += 1

    print('6.2.', odpady)

    kontr = 0
    for y in range(len(piksele)):
        for x in range(len(piksele[0])):

            if y < len(piksele)-1 and abs(piksele[y][x] - piksele[y+1][x]) > 128:
                kontr += 1
                continue

            if y > 0 and abs(piksele[y][x] - piksele[y-1][x]) > 128:
                kontr += 1
                continue

            if x < len(piksele[0])-1 and abs(piksele[y][x] - piksele[y][x+1]) > 128:
                kontr += 1
                continue

            if x > 0 and abs(piksele[y][x] - piksele[y][x-1]) > 128:
                kontr += 1
                continue

    print('6.3.', kontr)

    maks_len = 0
    temp_len = 0
    last = piksele[0][0]
    for x in range(len(piksele[0])):
        for y in range(len(piksele)):
            curr = piksele[y][x]

            if last == curr:
                temp_len += 1
                if temp_len > maks_len:
                    maks_len = temp_len

            else:
                temp_len = 1

            last = curr

    print('6.4', maks_len)
