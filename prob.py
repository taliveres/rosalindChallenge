from math import log10

def count_base_prob(s, gc):
    a_t = ((1 - gc)/2)**(s.count("A") + s.count("T"))
    c_g = (gc/2)**(s.count("C") + s.count("G"))#(len(s) - a_t)
    return '%.3f' % log10(a_t*c_g)#round(log10(a_t*c_g), 3)


file_path = r"C:\Users\natas\Downloads\rosalind_prob.txt"

f = open(file_path, "r")

s = f.readline()

gcProbs = [float(x) for x in f.readline().split()]

log_probs = [count_base_prob(s, x) for x in gcProbs]

print(*log_probs)
