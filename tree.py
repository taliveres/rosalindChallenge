file = open(r"C:\Users\natas\Downloads\rosalind_tree.txt")

n = int(file.readline())

#to be connected, a graph with n nodes must have n-1 edges
neighbors = []

for line in file.readlines():
    neighbors.append(line.split())

print((n-1) - len(neighbors))




