def inversionCount(arr, n): #!MY CODE - Time limit exceeded
    # Your Code Here
    rev = 0
    for i in range(n):
        for j in arr[i+1:]:
            if arr[i]>j:
                rev+=1
    return rev
