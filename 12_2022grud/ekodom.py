from datetime import *

def log(tab):

    keys = list(tab.keys())

    print(keys)
    for i in range(len(tab[keys[0]])):
        for key in keys:
            print(tab[key][i], end='  ')
        
        print()


if __name__ == "__main__":

    tabela = {
        'id': [],
        'data': [],
        'retencja': [],
    }

    with open('ekodom.txt') as file:
        file.readline()
        id = 0

        for line in file:

            data, retencja = line.strip().split()

            d, m, y = list(map(lambda x: int(x), data.split('.')))
            

            tabela['id'] += [id]
            id += 1
            
            tabela['data'] += [datetime(y, m, d)]
            tabela['retencja'] += [int(retencja)]
    
    tabela.update({'zuzycie': []})

    for data in tabela['data']:
        tabela['zuzycie'] += [190 if data.strftime('%w') != '3' else 260]

        #niedziela poniedzialek wtorek sroda czwartek piatek sobota


    tabela.update({'podlewanie': [0 for i in tabela['id']]})
    for id in tabela['id']:

        if datetime(2022, 4, 1) <= tabela['data'][id] <= datetime(2022, 9, 30) and sum(tabela['retencja'][id-4: id]) <= 0 and sum(tabela['podlewanie'][id-4: id]) <= 0:

            tabela['podlewanie'][id] = 1
        else:
            tabela['podlewanie'][id] = 0

    for id in tabela['id']:
        if tabela['podlewanie'][id] == 1:
            tabela['zuzycie'][id] += 300


    start = ''
    end = ''
    dni = 0

    maks_dni = 0
    maks_start = ''
    maks_end = ''

    for id in tabela['id']:

        if dni == 0:
            start = tabela['data'][id]

        if tabela['retencja'][id] == 0:
            dni += 1
            end = tabela['data'][id]
        else:
            dni = 0
            continue

        if dni > maks_dni:
            maks_dni = dni
            maks_start = start
            maks_end = end


    wykres = {}
    for month in range(1, 13):

        days = list(filter(lambda x: int(tabela['data'][x].strftime('%m')) == month, tabela['id']))

        suma = sum(list(map(lambda x: tabela['retencja'][x], days)))

        wykres.update({month: suma})
        
    
    brak_wody = 0
    wodociag = 0

    tabela.update({'zbiornik': [0 for i in tabela['id']]})

    tabela['zbiornik'][0] = 5000
    for id in tabela['id'][1:]:

        tabela['zbiornik'][id] = tabela['zbiornik'][id-1] + (tabela['retencja'][id-1]-tabela['zuzycie'][id-1])

        if tabela['zbiornik'][id] <= 0:
            brak_wody += 1
            wodociag += abs(tabela['retencja'][id-1]-tabela['zuzycie'][id-1])

        


    log(tabela)

    print( 'Zad 4.1 a' , maks_dni, maks_start, maks_end)
    print( 'Zad 4.1 b', sum(tabela['podlewanie']))

    print(' Zad 4.3 ', brak_wody, wodociag)

    print(wykres)

