file_path = r"C:\Users\natas\Downloads\rosalind_fibd.txt"

f = open(file_path, "r")

#n is the nr of months, m is life expectancy
n, m = list(map(int, f.readline().strip().split()))

#Nr of pairs per month
months = []

for i in range(n):
    if i < 2:
        months.append(1)
    #No deaths before m months passed
    elif i < m:
        months.append(months[i - 2] + months[i - 1])
    elif i == m or i == m + 1:
        months.append(months[i - 2] + months[i - 1] - 1)
    else:
        months.append(months[i - 2] + months[i - 1] - months[i - m - 1])


#print(fib(int(n_m[0]), int(n_m[1])))
print(months)
