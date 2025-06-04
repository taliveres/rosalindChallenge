file_path = r"C:\Users\natas\Downloads\rosalind_grph.txt"

f = open(file_path, "r")

seqs = {}
seq = ""
id_seq = f.readline()[1:].strip()

for x in f:
    if x[0] == '>':
        if seq != "":
            seqs[id_seq] = seq
            id_seq = x[1:].strip()
        seq = ""
    else:
        seq += x.strip()
seqs[id_seq] = seq

overlap = []

#compare all suffixes to prefixes of other sequences
for key in seqs:
    id_seq = key
    suf = seqs[key][-3:]
    for seq in seqs:
        if seq != id_seq:
            if seqs[seq][:3] == suf:
                overlap.append([id_seq, seq])

[print(*x) for x in overlap]




