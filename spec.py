from massDict import *

file_path = r"C:\Users\natas\Downloads\rosalind_spec.txt"

mass_dict = mass_dict()

rev_mass_dict = {round(v, 4): k for k, v in mass_dict.items()}

masses = []

for line in open(file_path):
    masses.append(float(line.strip()))

n = len(masses)

s = ''

for i in range(n - 1, 0, -1):
    diff = round(masses[i] - masses[i-1], 4)
    s += rev_mass_dict.get(diff)

print(s[::-1])
