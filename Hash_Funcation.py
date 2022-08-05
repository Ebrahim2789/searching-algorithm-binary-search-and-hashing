import json
import time as t
def Sortfile():
    with open('file1.txt.', 'r', encoding='UTF-8') as f:
        datafile = f.readlines()
        # print(datafile)
        data = len(datafile)
        print(data)
        rows = []
        with open('temp1.txt', 'w', encoding='UTF-8') as f1:
            for line in datafile:
                value = line.split()
                json_str = json.dumps(value)
                resp = json.loads(json_str)
                lan = len(value)
                for i in range(len(value)):
                    print(resp[i], ',', i, file=f1)

    with open('temp1.txt', 'r', encoding='UTF-8') as f1:
        sortd = f1.readlines()
        sorted_word = sorted(sortd)
        with open('temp2.txt', 'w', encoding='UTF-8') as f2:
            for l in sorted_word:
                v, k = l.strip().split(',', 1)
                nxt = int(k)
                print(v, ',', k, ',', nxt + 1, file=f2)


def Build_hash(phares):
    f4 = open(file='hashtime.txt', mode='w', encoding='UTF-8')
    with open('temp2.txt', 'r', encoding='UTF-8') as f2:
        outputs = f2.readlines()
        lengs = len(outputs)
        v = phares.strip().split(' ')
        valulang = len(v)
        with open('Hasht.txt', 'w', encoding='UTF-8') as f3:
            for k in range(valulang):
                count = 0
                indext = []
                for i in range(lengs):
                    if outputs[i].find(v[k]) != -1:
                        w, fin= outputs[i].strip().split(',', 2)
                        print(fin, file=f3)
                        print(w, ',', fin,  file=f4)
                        # print(w, fin, ind)
                        count = count + 1

                    else:
                        continue
                print(v[k], count, file=f4)
                print(v[k], count, file=f5)


def searchs(phares):
    start = t.time()
    with open('Hasht.txt', 'r', encoding='UTF-8') as f3:
        fanal = f3.readlines()
        fanallang = len(fanal)
        finalsorted = sorted(fanal)
        end = fanallang - 1
        d = 0
        while d < end:
            if int(finalsorted[d + 1]) == int(finalsorted[d]) + 1:
                print(t.time() - start, file=f5)
                v = phares.strip().split(' ')
                valulang = len(v)
                for k in range(valulang):
                    print(v[k], finalsorted[d])
                break
            else:
                d = d + 1


if __name__ == "__main__":
    f5 = open(file='hello.txt', mode='a', encoding='UTF-8')
    phares = 'Kitaabonni Afaan '
    # Build_hash(phares)
    searchs(phares)
    # Sortfile()
