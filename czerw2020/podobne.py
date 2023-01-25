# 5. Prawda
# 6. k = 4
# 7. Fałsz



def czy_k_podobne(n, A, B, k):
    # A[1 : k] == B[n - k + 1 : n] and A[k + 1 : n] == B[1, n-k]

    podobne = True
    for kv in range(0, k ):
        # print(A[1 + kv] , B[n - k + 1 + kv])

        if A[1 + kv] != B[n - k + 1 + kv]:
            podobne = False
            break
    
    
    for kv in range(0, k+1):
        # print(A[k + 1 + kv], B[kv + 1])

        if A[k + 1 + kv] != B[kv + 1]:
            podobne = False
            break
    
    return podobne
    
def czy_podobne(n , A, B):

    return any([czy_k_podobne(n, A, B, i) for i in range(n)])




# a = [5,7,9]
# b = [5,7,9]
a = [4, 2, 4, 4, 2, 6] 
b = [4, 4, 2, 6, 4, 2] 

A = {i+1: v for i, v in enumerate(a)}
B = {i+1: v for i, v in enumerate(b)}

k = 1

print(czy_k_podobne(len(a), A, B, k))
print(czy_podobne(len(a), A, B))