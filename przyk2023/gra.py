
class matureList:
    lista = []
    def __init__(self, iterable: list) -> None:
        self.lista = iterable

    def at(self, i: int):
        return self.lista[i-1]

    def set(self, value: any,  i: int):
        self.lista[i-1] = value

    def len(self):
        return len(self.lista)

    def print(self):
        print(self.lista)


if __name__ == '__main__':

    dane = [
        [[1,2,3], 5],
        [[1,2,5,10], 14],
        [[13,5,5,2,7], 17],
        [[7,6,5,4,3,2,1], 25],
        [[i for i in range(5, 101, 5)], 500]
    ]

    for d in dane:
        s = d[1] 
        B = [False for i in range(s+1)] 
        A = {i+1: d[0][i] for i in range(len(d[0]))}
        n = len(A) 

        B[0] = True 

        def Tura(k):

            for i in range(s, A[k]-1, -1):

                if B[i - A[k]] and not B[i]:
                    B[i] = True

            

        for k in range(1, n+1):
            Tura(k)

        print(d,'Wygrana?', B[s])

        if d[1] == 500:

            print('Zad 2.2', B.count(True))
