def dflag_sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while(mid<=high):
        if(arr[mid]==0):
            arr[mid],arr[low] = arr[low],arr[mid]
            low+=1
            mid+=1
        elif(arr[mid] == 2):
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
        else:
            mid+=1

def main():
    arr = [2,0,1,1,0,0,0,2,2,2,1]
    for i in arr:
        print(i, end=" ")
    dflag_sort(arr)
    print("\nSorted array is:")
    for i in arr:
        print(i, end=" ")

if(__name__ == "__main__"):
    main()