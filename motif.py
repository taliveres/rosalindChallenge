import re

file_path = r"C:\Users\natas\Downloads\rosalind_subs (1).txt"

f = open(file_path, "r")
seq = f.readline()
print(seq)
motif = f.readline().strip()
print(motif)
pos = ""

'''for i in range(len(seq) - len(motif)):
    sub = seq[i:i+len(motif)]
    print(sub)
    if sub == motif:
        pos += str(i + 1)
        pos += " "'''


for m in re.finditer(rf"(?={motif})", seq):
    pos += str(m.start() + 1)
    pos += " "


print(pos)

