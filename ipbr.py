k, m, n = map(int, input().split())

def MendProb(k,m,n):
    total_pairs= (((k+m+n)*(k+m+n -1 ))/2)
    
    kk_cont = (k*(k - 1))/2 
    km_cont = (k*m) 
    kn_cont = (k*n)
    mm_cont = (m*(m - 1))/2 * 3/4
    mn_cont = (m*n)/2
    tot_prob = kk_cont + km_cont + kn_cont + mm_cont + mn_cont

    return tot_prob/total_pairs

result = MendProb(k,m,n)
print(result)
