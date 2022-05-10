def neg_beg(arr): #!MY CODE
    i, j = 0, 0
    while j<len(arr):
        if arr[j] >= 0:
            j+=1
        elif arr[j] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
            i+=1
    print(arr)

def dutch_neg_beg(arr):
    low, mid = 0,0
    high = len(arr) - 1
    while(mid<=high):
        if arr[mid] < 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] > 0:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1
        else:
            mid+=1


def main():
    nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(nums)
    dutch_neg_beg(nums)
    # for k in range(len(op)):
    #     print(op[k])


if __name__ == "__main__":
    main()

