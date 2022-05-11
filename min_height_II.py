def getMinDiff(self, arr, n, k):
    # code here
    x = sorted(arr)
    
    ans = x[n-1] - x[0]
    
    small = x[0] + k
    large = x[n-1] - k
    mn, mx = 0,0

    for i in range(n-1):
        mn = min(small, x[i+1]-k)
        mx = max(large, x[i]+k)
        if mn<0: continue
        ans = min(ans, mx-mn)

    return(ans)