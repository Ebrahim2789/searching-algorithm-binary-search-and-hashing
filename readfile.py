# import json
# import os
# import time as t
# import csv
# import numpy
#
# start = t.time()
#
# # def DCS(P,daata):
# #     if P == 50:
# #         return S(P,daata)
# #     else:
# #         data = P // 20  # into smaller instances P1, P2 …, Pk
# #         p1 = data
# #         p2 = p1 + p1
# #         p3 = p2 + p1
# #         return C(p1,0), C(p2,p1), C(p3,p2)  # apply DCS to each of these sub-problems
# # def S(P,daata,f):
# #     print(P)
# #
# # def C(P,p1):
# #     print(P)
# #
# #     for line in daata:
# #         value = line.split()
# #         json_str = json.dumps(value)
# #         resp = json.loads(json_str)
# #         lan = len(value)
# #         if line == P:
# #             break
#
#
#
#
# def sortfile():
#     datafile = f.readlines()
#     # print(datafile)
#     data = len(datafile)
#     print(data)
#     value = []
#     for line in datafile:
#         value = line.split()
#         json_str = json.dumps(value)
#         resp = json.loads(json_str)
#         lan = len(value)
#         for i in range(len(value)):
#             rows = [[resp[i], i]]
#             # print(resp[i], ',', i, file=f1)
#
#     sortd = f1.readlines()
#     sorted_word = sorted(sortd)
#     print(len(sortd))
#     for l in sorted_word:
#         v= l.split()
#         # nxt = int(k)
#         print(v,  file=f2)
#
# def binary_search(output,low,avarege,high,lsn):
#     v = lsn.strip().split(' ')
#     valulang=len(v)
#     for k in range(valulang):
#         while low <high:
#             if lsn[0]==output[avarege][0]:
#                 if output[low].find(v[k]) != -1:
#                     print(output[low])
#                     break
#             elif lsn[0]<output[avarege][0]:
#                 if output[low].find(v[k]) != -1:
#                     print(output[low])
#                     break
#                 else:
#                     low = low + 1
#                 high = avarege - 1
#                 continue
#             else:
#                 low=avarege
#                 avarege=high
#                 binary_search(output, low, avarege, high, lsn)
#                 break
# if __name__ == "__main__":
#     f= open(file='file1.txt', mode='r', encoding='UTF-8')
#     f1 = open(file='temp1.txt', mode='r+', encoding='UTF-8')
#     f2 = open(file='temp2.txt', mode='r+', encoding='UTF-8')
#     f3 = open(file='temp3.txt', mode='w', encoding='UTF-8')
#     sortfile()
#     output = f2.readlines()
#     leng = len(output)
#     avarege = leng // 2
#     low = 0
#     high = leng - 1
#     phras = 'armaan'
#     binary_search(output, low, avarege, high, phras)
#
#
#
#
#
# from heapq import heappop
# import heapq as hp
#
# def heapsort(iterable):
#         h = []
#         for value in iterable:
#              hp.heappush(h, value)
#         print(h)
#         print( [hp.heappop(h) for i in range(len(h))])
#
# if __name__ == "__main__":
#     with open('hellod.txt', 'w', encoding='UTF-8') as f2:
#
#             # print(value)
#         hk=['osmaa','abdii','kana']
#         print(hk,file=f2)
#         # heapsort(value[0])

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# mean() Arithmetic mean (“average”) of data.
# fmean() Fast, floating point arithmetic mean.
# geometric_mean() Geometric mean of data.
# harmonic_mean() Harmonic mean of data.
# median() Median (middle value) of data.
# median_low() Low median of data.
# median_high() High median of data.
# median_grouped() Median, or 50th percentile, of grouped data.
# mode() Single mode (most common value) of discrete or nominal data.
# multimode() List of modes (most common values) of discrete or nomimal data.
# quantiles() Divide data into intervals with equal probability
import statistics as stat
print(stat.mean([1, 2, 3, 4, 4]))
print(stat.median([1, 2, 3, 4, 4]))
print(stat.mode([1, 2, 3, 4, 4]))

# import mmap
#
# # write a simple example file
# with open("hello.txt", "wb") as f:
#     f.write(b"Hello Python!\n")
#
#
# with open("hello.txt", "r+b") as f:
#     # memory-map the file, size 0 means whole file
#     mm = mmap.mmap(f.fileno(), 0)
#
#     print(len(mm))
#     # read content via standard file methods
#     print()  # prints b"Hello Python!\n"
#     # read content via slice notation
#     # print(mm[:5])  # prints b"Hello"
#     # # update content using slice notation;
#     # # note that new content must have same size
#     # mm[6:] = b" world!\n"
#     # # ... and read again using standard file methods
#     # mm.seek(0)
#     # print(mm.readline())  # prints b"Hello  world!\n"
#     # close the map
#     mm.close()


