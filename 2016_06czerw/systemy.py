def z(n): print(f'Zad 6.{n}')
kody = [line.strip() for line in open('liczby.txt', 'r')] 
liczby = [ [int(n[:-1]) , int(n[-1]) ] for n in kody]
z(1); print(len([1 for n, p in liczby if p == 8]))
z(2); print(len([1 for n, p in liczby if p == 4 and '0' not in str(n)]))
z(3); print(len([1 for n, p in liczby if p == 2 and n % 2 == 0]))
z(4); print(sum([int(str(n), 8) for n, p in liczby if p == 8]))
z(5); print('Kod / Dec')
dec = [int(str(n), p) for n, p in liczby]
maks, mini = dec.index(max(dec)), dec.index(min(dec))
print('max', kody[maks], dec[maks])
print('min', kody[mini], dec[mini])