


def sito(n):

    A = [True]*(n+1)
    A[0] = False
    A[1] = False
    k = 2

    while k <= n:

        if k:
            j = k
            while j + k <= n:
                j += k
                A[j] = False

        k += 1

    return A

def czworacze(n, primes):

    w = 0
    lista = []

    i = 0

    while w <= n:

        temp = [i, i+2, i+6, i+8]

        if primes[temp[0]] and primes[temp[1]] and primes[temp[2]] and primes[temp[3]]:
            lista.append(temp)
            w += 1

        i += 1

    return lista


if __name__ == '__main__':


    primes = sito(10000)
    
    c = czworacze(3, primes)

    print(c)
        
