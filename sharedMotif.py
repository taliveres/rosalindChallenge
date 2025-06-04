file_path = r"C:\Users\natas\Downloads\rosalind_lcsm.txt"

f = open(file_path, "r")

seqs = []
seq = ""
motif = ""

for x in f:
    if x[0] == '>':
        if seq != "":
            seqs.append(seq)
        seq = ""
    else:
        seq += x.strip()
seqs.append(seq)

#Compare all sequences to first, motif must exist in all
s = seqs[0]

#start from first base
for i in range(len(s)):
    #j is length of k-mer
    for j in range(len(s) - i + 1):
        if j > len(motif):
            m = s[i : i + j]
            #if k-mer in all seqs & longer than previously found motif
            if all(m in k for k in seqs):
                motif = m

print(motif)
