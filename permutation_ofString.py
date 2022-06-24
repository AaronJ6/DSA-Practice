def find_permutation(S):
    # Code here
    sList = list(S)
    sList.sort()
    res = []
    
    def permute(a, l, r):
        if l>=r:
            str_pr = ''.join(a)
            if str_pr not in res:
                res.append(str_pr)
        
        else:
            for i in range(l,r):
                a[l], a[i] = a[i], a[l]
                permute(a,l+1,r)
                if l!=0:
                    a[l], a[i] = a[i], a[l]

    n = len(S)
    permute(sList, 0, n)
    return res