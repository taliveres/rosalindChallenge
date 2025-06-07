file = open(r"C:\Users\natas\Downloads\rosalind_sset.txt")

n = int(file.readline())

print(2**n % 1000000)
