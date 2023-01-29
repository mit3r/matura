
count_p, count_k = 0,0

war = 0


def F(T, x):
    global count_p, count_k, war

    p = 1
    k = len(T)

    while p <= k:
        war += 1
        s = (p+k) // 2
        print(s)

        if T[s] == x:
            return True

        if T[s] < x:
            p = s + 1
            count_p += 1
        else:
            k = s - 1
            count_k += 1

    return False


T = {i+1: v for i, v in enumerate([3, 5, 7, 8, 90, 13, 33, 37, 40, 43])}

# T = {i+1: 0 for i in range(0, 100)}
# print(len(T))
print(F(T, 43))

# print('war', war)

# for x in [7, 43]:
#     print('dla x:', x)

#     count_k, count_p = 0, 0

#     print(F(T, x))
#     print('k, p:', count_k, count_p)

# Prawda
# x 7 43 
# p 1 3
# k 1 0
# 5 2 3

# 7
# False
