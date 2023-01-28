
global T
global n

count_iters = 0


def modyfikuj(s, k):
    global count_iters
    global T
    count_iters += 1

    if s + k < n:
        modyfikuj(s + k, k)
        

    i = s + 1
    while i <= n and i <= s+k:
        T[s] = T[s] + T[i]
        i += 1 



if __name__ == '__main__':

    dane = [
        [8, [1, 1, 1, 1, 1, 1, 1, 1], 3, 3],
        [10, [1, 4, 2, 8, 3, 6, 2, 9, 1, 5], 5, 6],
        [13, [4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 3, 5],
        [13, [4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 4, 4],
    ]

    for n, tablica, s, k  in dane:

        T = {i+1: tablica[i] for i in range(len(tablica))}

        modyfikuj(s, k)

        print(list(T.values()))

    example = [1]*2200

    dane = [
        [5, example, 1, 3],
        [2021, example, 1, 100],
        [2021, example, 20, 35],
    ]

    for n, tablica, s, k  in dane:
        T = {i+1: tablica[i] for i in range(len(tablica))}

        count_iters = 0
        modyfikuj(s, k)

        print(n, count_iters)



        