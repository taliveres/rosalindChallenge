import re

codon_file_path = r"C:\Users\natas\Downloads\codons.txt"
file_path = r"C:\Users\natas\Downloads\rosalind_mrna.txt"
f = open(file_path, "r")
seq = f.readline().strip()

codon_prob = {}
cf = open(codon_file_path, "r")

for line in cf:
    keys = re.findall("\s[A-Z][^a-zA-Z]|Stop", line)
    for i in range(len(keys)):
        key = keys[i].strip()
        if key in codon_prob:
            codon_prob[key] += 1
        else:
            codon_prob[key] = 1

combis = 1

for aa in seq:
    combis *= codon_prob[aa]

print(combis * 3 % 1000000)

