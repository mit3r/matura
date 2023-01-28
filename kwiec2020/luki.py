


if __name__ == '__main__':

    ciag = [int(line.strip()) for line in open('dane4.txt', 'r')]

    luki = [abs(ciag[i] - ciag[i+1]) for i in range(0, len(ciag)-1)]

    print('Zad. 4.1')

    print(max(luki))
    print(min(luki))

    print('Zad. 4.2')

    last = -1
    temp_start = 0
    temp_end = 0
    temp_lenght = 1

    maks_start = 0
    maks_end = 0
    maks_lenght = 1

    for i, luka in enumerate(luki):

        if last != luka:
            temp_start = i
            temp_end = i
        else:
            temp_end = i

        last = luka
        temp_lenght = temp_end - temp_start + 1

        if temp_lenght > maks_lenght:
            maks_start = temp_start
            maks_end = temp_end
            maks_lenght = temp_lenght

    #długość fragmentu jest o 1 dłuższa
    print(maks_lenght+1)

    #funkcja fragmentu kończy na drugim a trzeba jesze 1 dodać
    z = ciag[maks_start : maks_end+2]
    print(z[0], z[-1])


    print('Zad 4.3')
    uniq = {l: luki.count(l) for l in luki}

    najkrot = max(uniq.items(), key=lambda x: x[1])[1]
    print(najkrot)

    luk_onajkrot = [luka for luka, krotnosc in uniq.items() if krotnosc == najkrot] 
    print(*luk_onajkrot)
