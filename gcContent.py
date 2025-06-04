import re

file_path = r"C:\Users\natas\Downloads\rosalind_gc.txt"
id_max = ""
id = ""
gc_cont_max = 0
seq = ""

def count_gc(seq, id):
    global gc_cont_max
    global id_max
    gc_cont = len(re.findall("[GC]", seq)) / len(seq)*100
    if gc_cont > gc_cont_max:
        gc_cont_max = gc_cont
        id_max = id

f = open(file_path, "r")
for x in f:
  if x[0] == '>':
      if seq != "":
          count_gc(seq, id)
      seq = ""
      id = x[1:]
  else:
      seq += x.strip()
count_gc(seq, id)

print("ID: " + id_max)
print("GC content: " + str(round(gc_cont_max, 6)))



