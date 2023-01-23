import random
if __name__ == '__main__':

    for ran in range(100):
        g = random.randint(1, 10)
        
        iter = []
        for h in range(g):
            iter.append(int(random.random()*1000))

        for s in range(1, 201):
            B = [False for i in range(s+1)] 
            A = {i+1: iter[i] for i in range(len(iter))}
            n = len(A) 

            B[0] = True 

            def Tura(k):

                for i in range(s, A[k]-1, -1):

                    if B[i - A[k]] and not B[i]:
                        B[i] = True

                

            for k in range(1, n+1):
                Tura(k)

            if not B[s]:
                break

            if s == 200:
                print(iter)
