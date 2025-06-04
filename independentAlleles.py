import scipy

file_path = r"C:\Users\natas\Downloads\rosalind_lia.txt"

f = open(file_path, "r")

k, n = list(map(int, f.readline().strip().split()))

sum = 0

#Add up probability of less than N offspring with AaBb genotype
for i in range(n):
    #Total nr of offspring is 2**k, prob of AaBb offspring always 0.25 (Punett Square)
    sum += scipy.stats.binom.pmf(i, 2**k, 0.25)

#Prob of at least N AaBb offspring is complement
print(round(1-sum, 3))

