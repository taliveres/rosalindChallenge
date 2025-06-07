from massDict import *
from conv import *

file = open(r"C:\Users\natas\Downloads\rosalind_prsm.txt")

n = int(file.readline())

prots = []
masses = []

while len(prots) < n:
    prots.append(file.readline().strip())

for line in file:
    masses.append(line.strip())

mass_dict = mass_dict()

def get_complete_spec(s):
    complete_spec = []
    weights = []
    for aa in s:
        weights.append(mass_dict[aa])
    for i in range(len(s) - 1):
        complete_spec.append(sum(weights[:i + 1]))
        complete_spec.append(sum(weights[i + 1:]))

    return complete_spec

mult = {}
for prot in prots:
    prot_spec = get_complete_spec(prot)
    mult[prot] = get_max_mult(masses, prot_spec)

print(max(mult.values()))
print(max(mult, key=mult.get))

