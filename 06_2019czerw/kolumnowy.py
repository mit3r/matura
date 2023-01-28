

def decode_kolumnowy(k, n, S):

    wiersz = len(S) // k
    
    tab = [S[i*wiersz : (i+1)*wiersz] for i in range(0, k)]

    tab = [[c[w] for c in tab] for w in range(len(tab[0]))]

    tab = [line[::-1] if i % 2 else line for i, line in enumerate(tab)]
    tab = [*map("".join, tab)]
    tab = "".join(tab)

    print(tab)

S = 'NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P '

decode_kolumnowy(10, len(S), S)

# P F P F
# P F P F

# F F F P