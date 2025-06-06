from massDict import *
from collections import defaultdict
file = open(r"C:\Users\natas\Downloads\rosalind_sgra.txt")

mass_dict = mass_dict()

rev_mass_dict = {round(v, 4): k for k, v in mass_dict.items()}

masses = []

for line in file.readlines():
    masses.append(float(line.strip()))

def get_graph(masses, rev_mass_dict):
    graph = defaultdict(list)
    for i in range(len(masses) - 1):
        for j in range(len(masses)):
            diff = round(masses[j] - masses[i], 4)
            if rev_mass_dict.get(diff):
                graph[masses[i]] += [[masses[j], rev_mass_dict.get(diff)]]  #print('i: ' + str(i + 1) + ' j: ' + str(j + 1) + ', AA: ' + str(rev_mass_dict.get(diff)))
    return graph


graph = get_graph(masses, rev_mass_dict)

s = ''

def get_seqs(weight, s):
    for pairedWeight, aa in graph[weight]:
        yield from get_seqs(pairedWeight, s + aa)
    yield s

seqs = list(get_seqs(min(masses), s))
print(max(seqs, key=len))

