
def Count_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        key = i
        while key > 0 and arr[key] < arr[key-1]:
            arr[key-1], arr[key] = arr[key], arr[key-1]
            swaps += 1
            key -= 1
    
    return swaps  

if __name__ == "__main__":
    with open('/home/elenadg04/PoC2/rosalind_ins (5).txt', 'r') as f:
        f.readline()
        j = [int(i) for i in f. readline().strip().split(' ')]
        print(Count_swaps(j))