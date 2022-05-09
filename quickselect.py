# average case is O(n)
# worst case is O(n^2)

def partition(arr,low,high): #!MY CODE
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if(arr[j] <= pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return(i+1)

def quickselect(arr,low,high, k): #!MY CODE - WRONG for case [2,1] k = 2
    if(len(arr) == 1):
        return arr[0]
    if low < high:
        pi = partition(arr,low,high)
        chk = len(arr) - k
        if(chk == pi):
            op = arr[pi]
        elif(chk<pi):
            op = quickselect(arr,low,pi-1, k)
        else:
            op = quickselect(arr,pi+1,high, k)
        return op

def quickSelect(arr,low,high,k): #!NeetCode CODE
    pivot,p = arr[high], low
    for i in range(low,high):
        if arr[i]<=pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    arr[p],arr[high] = arr[high],arr[p]

    if p>k:     return(quickSelect(arr,low,p-1,k))
    elif p<k:   return(quickSelect(arr,p+1,high,k))
    else:       return(arr[p])

def main():
    arr = [3,2,1,5,6,4]
    n = len(arr)
    k = int(input())
    k = len(arr) - k
    op = quickSelect(arr, 0 , n-1, k)
    print(op)

if(__name__ == "__main__"):
    main()