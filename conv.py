file = open(r"C:\Users\natas\Downloads\rosalind_conv.txt")

s1 = file.readline().split()
s2 = file.readline().split()

def get_max_mult(s1, s2):
    mass_diffs = {}

    for mass1 in s1:
        for mass2 in s2:
            diff = round(abs(float(mass1) - float(mass2)), 5)
            if diff in mass_diffs:
                mass_diffs[diff] += 1
            else:
                mass_diffs[diff] = 1

    #return mass_diffs
    return max(mass_diffs.values())


get_max_mult(s1, s2)

