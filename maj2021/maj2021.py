



def dopisz(napis, arg):
    return napis + arg


def zmien(napis, arg):
    return napis[:-1] + arg

def usun(napis, number):
    number = int(number)
    return napis[:-number]

def przesun(napis, arg):

    index = napis.find(arg)
    if index == -1:
        return napis

    napis = list(napis)
    char = napis[index]
    char = 'A' if ord(char) + 1 > ord('Z') else chr(ord(char) + 1)

    napis[index] = char
    return "".join(napis)

komendy = {
    'DOPISZ': dopisz,
    'ZMIEN': zmien,
    'USUN': usun,
    'PRZESUN': przesun,
}

if __name__ == '__main__':

    napis = ''

    with open('./przyklad.txt', 'r') as file:
        for linia in file:
            kom, arg = linia.split()
            napis = komendy[kom](napis, arg)

    print(napis)
        


        

        


        