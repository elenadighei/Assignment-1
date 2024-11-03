s = input()
sc = ''

for nucleotide in s:
    if nucleotide == 'A':
        sc += 'T'
    elif nucleotide == 'T':
        sc += 'A'
    elif nucleotide == 'C':
        sc += 'G'
    elif nucleotide == 'G':
        sc += 'C'
result = sc[::-1]
print(result)