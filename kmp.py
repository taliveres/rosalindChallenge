from readFasta import *

file_path = r"C:\Users\natas\Downloads\rosalind_kmp.txt"

seq = list(readFasta(file_path).values())[0]

j = -1
p = [j]


for i in range(len(seq)):
    while j >= 0 and seq[i] != seq[j]:
        j = p[j]
    j += 1
    p.append(j)

print(*p[1:])


