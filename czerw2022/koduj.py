
def Koduj(n):

    if n == 1:
        return ''
    else:
        k = n // 2
        if k % 2 == 0:
            return Koduj(k) + 'A'
        else:
            return 'B' + Koduj(k)

def KodujWyw(n, wyw):

    if n == 1:
        return ''
    else:
        wyw[0] += 1
        k = n // 2
        if k % 2 == 0:
            return KodujWyw(k, wyw) + 'A'
        else:
            return 'B' + KodujWyw(k, wyw)


if __name__ == '__main__':
    

    # for n in [1, 2, 12, 33, 1022]:
    #     wyw = [1]
    #     print(n, KodujWyw(n, wyw),wyw[0])

    for i in range(100):
        for u in range(100):

            if u == i:
                continue
            
            try:

                first, second = Koduj(i), Koduj(u)

                if first == second and len(first) == 6 and len(second) == 6:
                    print(i, u)

            except:
                continue



    

