def mass_dict():
    masses_path = r"C:\Users\natas\Downloads\rosalind_monoiso.txt"
    masses = open(masses_path, "r")

    mass_dict = {}

    for line in masses:
        mass_dict[line[:1]] = float(line[1:].strip())

    return mass_dict