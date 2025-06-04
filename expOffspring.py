file_path = r"C:\Users\natas\Downloads\rosalind_iev.txt"

f = open(file_path, "r")

pairings = list(map(int, f.readline().strip().split()))

offspr = []

for i in range(6):
    if pairings[i] > 0:
        if i <= 2: offspr.append(pairings[i]) #Genotypes AA-AA, AA-Aa, AA-aa, P(dom) = 1
        if i == 3: offspr.append(pairings[i]*0.75) #Genotype Aa-Aa, P(dom) = 0.75
        if i == 4: offspr.append(pairings[i] * 0.5) #Genotype Aa-aa, P(dom) = 0.5
        #Genotype aa-aa has P(dom) = 0

#Every pair has 2 offspring
print(2*sum(offspr))