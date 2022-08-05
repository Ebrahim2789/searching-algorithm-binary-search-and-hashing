import json
import mmap
import os
import heapq as hp
import time as t
import numpy as np

start = t.time()


def Sortfile():
    with open('file3.txt.', 'r', encoding='UTF-8') as f:
        datafile = f.readlines()
        # print(datafile)
        data = len(datafile)
        print(data)
        value = []
        with open('temp1.txt', 'w', encoding='UTF-8') as f1:
            for line in datafile:
                value = line.split()
                json_str = json.dumps(value)
                resp = json.loads(json_str)
                lan = len(value)
                for i in range(len(value)):
                    rows = [[resp[i], i]]
                    print(resp[i], ',', i, file=f1)
    with open('temp1.txt', 'r', encoding='UTF-8') as f1:
        sortd = f1.readlines()
        sorted_word = sorted(sortd)
        with open('temp2.txt', 'w', encoding='UTF-8') as f2:
            for l in sorted_word:
                v, k = l.strip().split(',', 1)
                print(v, ',', k, file=f2)


def binary_search(output, low, avarege, high, lsn):
    start = t.time()
    v = lsn.strip().split(' ')
    valulang = len(v)
    for k in range(valulang):
        while low < high:
            if lsn[0] == output[avarege][0]:
                if output[low].find(v[k]) != -1:
                    print(output[avarege])
                    print(t.time() - start, ',', low, file=f3)
                    # memory_usage(avarege)
                    break
                else:
                    low = low + 1
            elif lsn[0] < output[avarege][0]:
                if output[low].find(v[k]) != -1:
                    print(output[low])
                    print(t.time() - start, ',', low, file=f3)
                    # memory_usage(low)
                    break
                else:
                    low = low + 1
                high = avarege - 1
                continue
            else:
                low = avarege
                avarege = high
                binary_search(output, low, avarege, high, lsn)
                break


def memory_usage():
    f3 = open(file='temp3.txt', mode='r', encoding='UTF-8')
    memoryu = f3.readlines()
    h= []
    for l in memoryu:
        v, k = l.split(',',1)
        print(np.round(v,2,2), k)

        indexs=int(v)
        hp.heappush(h, indexs)
    import statistics as stat
    print(stat.mean(h))
    print(stat.median(h))
    print(stat.mode(h))
        # with open("temp2.txt", "r+b") as f:
        #     mm = mmap.mmap(f.fileno(), indexs)
        #     bytess=len(mm)
        #     total_memory=mm.size()
        #     total_m_at_index=total_memory*bytess/leng
        #     print(total_m_at_index)
        #     print()
            # with open("hello.txt", "wb") as h:
            #     h.write(f.readlines())


if __name__ == "__main__":
    f3 = open(file='temp3.txt', mode='a', encoding='UTF-8')
    with open('temp2.txt', 'r', encoding='UTF-8') as f2:
        output = f2.readlines()
        leng = len(output)
        print(leng)
        avarege = leng // 2
        low = 0
        high = leng - 1
        bestcase = 'Afaan'
        avaregecase = 'hojjettoota'
        worestcase = 'zeyitiifi'
        # Sortfile()
        # binary_search(output,low,avarege,high,worestcase)
        memory_usage()

