sekwencje = [line.strip() for line in open('./sekwencje.txt')][:10]

print(sekwencje, len(sekwencje))


def czyDNA(napis):
    for znak in napis:
        if znak not in ('A', 'C', 'T', 'G'):
            return False
    return True


def czyRNA(napis):
    for znak in napis:
        if znak not in ('A', 'C', 'U', 'G'):
            return False
    return True


dna_arr = []
rna_arr = []

ile_dna = 0
ile_rna = 0

with open('./nic_matrycowa.txt', 'w') as plikDNA, open('./rna.txt', 'w') as plikRNA:
    for napis in sekwencje:
        if czyDNA(napis):
            plikDNA.write(napis + '\n')
            ile_dna += 1
            dna_arr += [napis]
        elif czyRNA(napis):
            plikRNA.write(napis + '\n')
            ile_rna += 1
            rna_arr += [napis]

print(f'Liczba znalezionych sekwencji DNA wynosi {ile_dna}.')
print(f'Liczba znalezionych sekwencji RNA wynosi {ile_rna}.')

with open('./wyniki_zad3.txt', 'w') as file:
    file.writelines([
        f'Liczba znalezionych sekwencji DNA wynosi {ile_dna}.\n',
        f'Liczba znalezionych sekwencji RNA wynosi {ile_rna}.\n',
    ])

dna_rna_dict = {
    'T': 'A',
    'A': 'U',
    'C': 'G',
    'G': 'C',
}


def dna_to_rna(napis):
    return ''.join([dna_rna_dict[znak] for znak in napis])


rna_dna_dict = {
    'A': 'T',
    'U': 'A',
    'C': 'G',
    'G': 'C',
}


def rna_to_dna(napis):
    return ''.join([rna_dna_dict[znak] for znak in napis])


with open('./rna_nowe.txt', 'w') as rna_nowe, open('./dna_nowe.txt', 'w') as dna_nowe:
    rna_nowe.writelines([f'{dna_to_rna(napis)}\n' for napis in dna_arr])
    dna_nowe.writelines([f'{rna_to_dna(napis)}\n' for napis in rna_arr])
