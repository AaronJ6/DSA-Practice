def merge(arr1, arr2, n, m): #Just put all the small numbers in arr1 and rest in arr2 then sort and done
    # code here
    i = 0
    j = 0
    while i<n:
        mn = arr2.index(min(arr2))
        if arr1[i]>arr2[mn]:
            arr2[mn], arr1[i] = arr1[i], arr2[mn]
        i+=1
    arr1.sort()
    arr2.sort()