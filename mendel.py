import re
file_path = r"C:\Users\natas\Downloads\rosalind_iprb.txt"

f = open(file_path, "r")
set = re.split("\s", f.read())
k = int(set[0])
m = int(set[1])
n = int(set[2])

all = k + m + n #float(k*(k-1) + 2*k*m + 2*k*n + m*(m-1) + 2*m*n + n*(n-1))

rez = float(0.25*(m/all)*((m-1)/(all-1)) + 0.5*(m/all)*(n/(all-1)) + 0.5*(n/all)*(m/(all-1)) + (n/all)*((n-1)/(all-1)))

print(1 - float(rez))



