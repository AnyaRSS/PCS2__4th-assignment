from Bio import SeqIO
sequence = ''
for s in SeqIO.parse('rosalind_revp.txt', 'fasta'):
    sequence = s.seq
#print(sequence)

com = sequence.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

for x in range(len(sequence)):
    for y in range(x, len(sequence)):
        p = sequence[x : y+1]
        print(p)
        r = com[x : y+1]
        if len(p) >= 4 and len(p) <= 12:
            if p == r[::-1]:                
                print(x + 1, len(p))