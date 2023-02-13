from gprint import *




napis = ['bnśiwpażyłhęa', 'swazkąadctzya']

for line in napis:
    print(line[::3])


napis = ['cnśzwayźysłęteie', 'sakeądrczcyde']

for line in napis:
    gprint(line[::3], [255, 0, 0],)


[gprint('#####', [255-i, i, 255-i], False) for i in range(256)]