t = input()
u = ''

for nucleotide in t:
    if nucleotide == 'A':
        u += 'A'
    elif nucleotide == 'C':
        u += 'C'
    elif nucleotide == 'G':
        u += 'G'
    elif nucleotide == 'T':
        u += 'U'

print(u)