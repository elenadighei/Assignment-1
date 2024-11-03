s = input()
t = input()
indeces = (i for i, char in enumerate(s))

def DNAsubs(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            positions.append(i + 1) 
    return positions

positions = DNAsubs(s, t)
print(" ".join(map(str, positions)))