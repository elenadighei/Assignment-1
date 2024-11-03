s = input()

count_A = 0
count_C = 0
count_G = 0
count_T = 0

for nucleotide in s:
    if nucleotide == 'A':
        count_A += 1
    elif nucleotide == 'C':
        count_C += 1
    elif nucleotide == 'G':
        count_G += 1
    elif nucleotide == 'T':
        count_T += 1

print(count_A, count_C, count_G, count_T)