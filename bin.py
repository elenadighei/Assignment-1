def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid + 1  
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 
 
with open('/home/elenadg04/PoC2/rosalind_bins (2).txt', 'r') as infile:
    n = int(infile.readline().strip())  
    m = int(infile.readline().strip())  
    A = list(map(int, infile.readline().strip().split()))  
    keys = list(map(int, infile.readline().strip().split()))  


results = []
for key in keys:
    index = binary_search(A, key)
    results.append(index)


with open('/home/elenadg04/PoC2/rosalind_bins_output (2).txt', 'w') as outfile:
    outfile.write(' '.join(map(str, results)) + '\n')
