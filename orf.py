import re

codon_file_path = r"C:\Users\natas\Downloads\codons.txt"
file_path = r"C:\Users\natas\Downloads\rosalind_orf.txt"

seq = ''
with open(file_path, "r") as f:
    next(f)
    for line in f:
        seq += line.strip()

rna = seq.replace('T', 'U')

rna_c = ''
for base in seq[::-1]:
    if base == 'A':
        rna_c += 'U'
    elif base == 'C':
        rna_c += 'G'
    elif base == 'G':
        rna_c += 'C'
    elif base == 'T':
        rna_c += 'A'

codon_dict = {}
start = "AUG"
cf = open(codon_file_path, "r")

for line in cf:
    keys = re.findall("[UAGC]{3}", line)
    vals = re.findall("\s[A-Z][^a-zA-Z]|Stop", line)
    for i in range(len(keys)):
        val = vals[i].strip()
        codon_dict[keys[i]] = val

def find_seq(starts, rna):
    list = []
    for i in starts:
        prot = ""
        seq = rna[i.start():]
        done = False
        for j in range(0, len(seq), 3):
            if (j + 3) <= len(seq):
                cod = codon_dict[seq[j:j + 3]]
                if len(cod) != 1:
                    done = True
                    break
                prot += cod
        if prot != "" and done:
            list.append(prot)
    return list

all = []

if re.search("AUG", rna) is not None:
    start_pos = re.finditer("AUG", rna)
    all += find_seq(start_pos, rna)

if re.search("AUG", rna_c) is not None:
    start_pos_c = re.finditer("AUG", rna_c)
    all += find_seq(start_pos_c, rna_c)

for i in list(set(all)):
    print(i)




