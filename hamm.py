s=input()
t=input()

def DNADistance(s, t):
    result = 0
    for n in range(len(s)):
        if s[n] == t[n]:
           result += 0
        elif s[n] != t[n]:
           result += 1
    return result

print(DNADistance(s, t))