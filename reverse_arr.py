def rev(arr, start, end): #brute force
    if(start>=end):
        return
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    rev(arr, start+1, end-1)

def slicing(arr): #doesnt help since this does not change the position physically rather only printing
    print(arr[::-1])
    """ 2 syntaxes sequence[start:stop] and sequence[start:stop:step] 
    When you omit start, the value 0 is taken
    """

def main():
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    for i in arr:
        print(i, end = " ")
    rev(arr, 0, n-1)
    print("\n")
    for i in arr:
        print(i, end = " ")

if(__name__ == "__main__"):
    main()
