masses_path = r"C:\Users\natas\Downloads\rosalind_monoiso.txt"
file_path = r"C:\Users\natas\Downloads\rosalind_prtm.txt"

masses = open(masses_path, "r")
f = open(file_path, "r")
seq = f.read().strip()

mass_dict = {}

for line in masses:
    mass_dict[line[:1]] = float(line[1:].strip())

mass = 0

for aa in seq:
    mass += mass_dict[aa]

print(round(mass, 3))



