def merge(arr1, arr2, n, m): 
    # code here
    i = 0
    j = 0
    while i<n:
        mn = arr2.index(min(arr2))
        if arr1[i]>arr2[mn]:
            arr2[mn], arr1[i] = arr1[i], arr2[mn]
        i+=1
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    print(arr1, arr2)


arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
merge(arr1, arr2, 4, 5)