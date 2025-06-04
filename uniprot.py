from re import finditer
from urllib.request import urlopen
import re

file_path = r"C:\Users\natas\Downloads\rosalind_mprt.txt"

f = open(file_path, "r")

ids = list(f.read().splitlines())
proteins = []

for id in ids:
    proteins.append(id.split('_', 1)[0])

motif = re.compile("(?=N[^P][ST][^P])")

def get_seq(fasta):
    seq = fasta.split('\n', 1)[1].replace("\n", "")
    return seq

for prot in proteins:
    page = urlopen(f"http://www.uniprot.org/uniprot/{prot}.fasta")
    html = page.read().decode("utf-8")
    seq = get_seq(html)
    loc = []
    if motif.search(seq) is not None:
        print(prot)
        for ind in motif.finditer(seq):
            loc.append(ind.start() + 1)
        print(*loc)





