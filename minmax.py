def recur_minmax(arr, low, high): #recursive method
    mx = arr[low]
    mn = arr[low]

    if(low == high):
        return (mx,mn)
    elif(high == low + 1):
        mx = max(arr[low],arr[high])
        mn = min(arr[low], arr[high])
        return(mx,mn)
    else:
        mid = int((high+low)/2)
        mx1,mn1 = recur_minmax(arr, low, mid)
        mx2,mn2 = recur_minmax(arr,mid+1,high)
    
    return(max(mx1,mx2), min(mn1,mn2))

def getminMax(arr):
    n = len(arr)
    if(len(arr) == 1):
        return (arr[0],arr[0])
    elif(n == 2):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
    else:
        mx = arr[0]
        mn = arr[0]
        for i in range(1,len(arr)) :
            mx = max(arr[i], mx)
            mn = min(arr[i], mn)
    return(mx, mn)


def main():
    arr = [10,2,3,20,412,-1110,19]
    mx,mn = recur_minmax(arr,0,len(arr)-1)
    print("Max = ",mx, "\nMin = ",mn)


if(__name__ == "__main__"):
    main()


