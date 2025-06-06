def readFasta(file_path):

    f = open(file_path, "r")

    seqs = {}
    seq = ""
    id_seq = f.readline()[1:].strip()

    for x in f:
        if x[0] == '>':
            if seq != "":
                seqs[id_seq] = seq
                id_seq = x[1:].strip()
            seq = ""
        else:
            seq += x.strip()
    seqs[id_seq] = seq

    return seqs