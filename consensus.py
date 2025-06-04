file_path = r"C:\Users\natas\Downloads\rosalind_cons.txt"

f = open(file_path, "r")

seqs = []
seq = ""
conSeq = ""

for x in f:
    if x[0] == '>':
        if seq != "":
            seqs.append(seq)
        seq = ""
    else:
        seq += x.strip()
seqs.append(seq)

cons = {
    'A' : [0]*len(seqs[0]),
    'C' : [0]*len(seqs[0]),
    'G' : [0]*len(seqs[0]),
    'T' : [0]*len(seqs[0])
}

for i in range(len(seqs[0])):
    for seq in seqs:
        cons[seq[i]][i] += 1
    score = 0
    conB = ''
    for x in cons:
        if cons[x][i] > score:
            score = cons[x][i]
            conB = x
    conSeq += conB

print(conSeq)
for key, value in cons.items():
    print(key + ": " + ' '.join(str(v) for v in value))
