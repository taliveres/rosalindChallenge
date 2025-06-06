from massDict import *
from collections import defaultdict
file = open(r"C:\Users\natas\Downloads\rosalind_full.txt")

mass_dict = mass_dict()

rev_mass_dict = {round(v, 5): k for k, v in mass_dict.items()}

parent = float(file.readline())
masses = []

for line in file.readlines():
    masses.append(float(line.strip()))

masses.sort()

pairs = []

for i in range(len(masses) // 2):
    for j in range(len(masses)):
        if round(masses[i] + masses[j], 6) == round(parent, 6):
            pairs.append((masses[i], masses[j]))

s = ''

i = 0
while i < ((len(masses) - 2) // 2):
    diff = round(pairs[i + 1][0] - pairs[i][0], 5)
    if rev_mass_dict.get(diff):
        s += rev_mass_dict.get(diff)
        i += 1
    else:
        pairs[i + 1] = (pairs[i + 1][1], pairs[i + 1][0])
        pairs.sort()
        i = 0
        s = ''

print(s)




