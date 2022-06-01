def inversionCount(arr, n):
    # Your Code Here
    rev = 0
    for i in range(n):
        min = arr[i]
        post = i
        for j in range(i+1,n):
            if arr[j]<min:
                min = arr[j]
                post = j
        if min != arr[i]:
            arr[post], arr[i] = arr[i], arr[post]
            rev+=1
    return rev

arr = [2,4,1,3,5]
op = inversionCount(arr, len(arr))
print(op)