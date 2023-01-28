with open('przyklad.txt', 'r') as f:
    napis = ""

    for line in f:
        instrukcja, *litera = line.split()

        if instrukcja == "DOPISZ":
            napis += litera[0]

        elif instrukcja == "ZMIEN":
            napis = napis[:-1] + litera[0]

        elif instrukcja == "USUN":
            if napis:
                napis = napis[:-1]

        elif instrukcja == "PRZESUN":
            index = napis.find(litera[0])

            if index >= 0:
                next_letter = chr((ord(litera[0]) - ord('A') + 1) % 26 + ord('A'))
                napis = napis[:index] + next_letter + napis[index + 1:]

        print(napis)
