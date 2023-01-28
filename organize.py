
import os


months = {'marzec': 3, 'kwiec': 4, 'maj': 5, 'czerw': 6, 'lipiec': 7,
          'wrze': 9, 'listopad': 11, 'grud': 12}

if __name__ == '__main__':

    curdir = os.path.curdir

    for folder in os.listdir(os.getcwd()):

        if not all([
            folder[-4:].isalnum(),
            4 < len(folder) <= 9,
            folder[:-4] in months.keys()
        ]):
            continue

        src = os.path.join(curdir, folder)

        year = folder[-4:]
        name = folder[:-4]
        month_num = str(months[name]) if months[name] > 9 else '0' + str(months[name])

        folder = year + '_' + month_num + name

        dist = os.path.join(curdir, folder)

        os.rename(src, dist)
