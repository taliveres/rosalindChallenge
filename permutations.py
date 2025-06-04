from itertools import permutations
file_path = r"C:\Users\natas\Downloads\rosalind_perm.txt"

f = open(file_path, "r")

num = int(f.read().strip())
nums = [x + 1 for x in range(num)]
perm = list(permutations(nums))

print(len(perm))
[print(*x) for x in perm]

