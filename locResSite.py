file_path = r"C:\Users\natas\Downloads\rosalind_revp.txt"

seq = ''
with open(file_path, "r") as f:
    next(f)
    for line in f:
        seq += line.strip()

def rev_comp(seq):
    dna_c = ''
    for base in seq[::-1]:
        if base == 'A':
            dna_c += 'T'
        elif base == 'C':
            dna_c += 'G'
        elif base == 'G':
            dna_c += 'C'
        elif base == 'T':
            dna_c += 'A'
    return dna_c

min = 4
max = 12

for i in range(len(seq)):
    for j in range(min, max + 1, 1):
        if seq[i : i + j] == rev_comp(seq[i : i + j]) and (i + j) <= len(seq):
            print(i+1, j)


