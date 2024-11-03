def Three_Par(a):
   pivot = a[0]
   smaller =[]
   equal = []
   larger = []

   for i in range(1, len(a)):
      if a[i] < pivot:
         smaller.append(a[i])
      elif a[i] == pivot:
         equal.append(a[i])
      else:
         larger.append(a[i])
    
   return smaller + equal + [pivot] + larger

if __name__ == '__main__':
    with open('/home/elenadg04/PoC2/rosalind_par3 (2).txt', "r") as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().strip().split(' ')]

b = Three_Par(a)

with open('/home/elenadg04/PoC2/rosalind_3par_output(4).txt', "w") as output_file:
        output_file.write(" ".join(map(str, b)))