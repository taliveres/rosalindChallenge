import re

codon_file_path = r"C:\Users\natas\Downloads\codons.txt"
file_path = r"C:\Users\natas\Downloads\rosalind_prot.txt"

codon_dict = {}
cf = open(codon_file_path, "r")
for line in cf:
    #line = line.strip()
    keys = re.findall("[UAGC]{3}", line)
    vals = re.findall("\s[A-Z][^a-zA-Z]|Stop", line)

    for i in range(len(keys)):
        val = vals[i].strip()
        codon_dict[keys[i]] = val


f = open(file_path, "r")
rna = f.read()
prot = ""
for i in range(0, len(rna), 3):
    if (i+3) <= len(rna):
        cod = codon_dict[rna[i:i + 3]]
        if len(cod) != 1:
            break
        prot += cod

print(prot)