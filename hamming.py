file_path = r"C:\Users\natas\Downloads\rosalind_hamm.txt"

f = open(file_path, "r")

s = f.readline()
t = f.readline()
ham = 0

for i in range(len(s)):
    if s[i] != t[i]:
        ham += 1

print(ham)