def mergeSort(nums, temp, l, r):
    inv = 0
    if l<r:
        mid = (l+r) // 2
        inv += mergeSort(nums, temp, l, mid)
        inv += mergeSort(nums, temp, mid+1, r)
        inv += merge(nums, temp, l, mid, r)
    return inv

def merge(nums, temp, l, mid, r):
    i = l
    j = mid+1
    k = l
    inv = 0
    while(i<=mid and j<=r):
        if nums[i]<=nums[j]:
            temp[k] = nums[i]
            i+=1
            k+=1
        else:
            temp[k] = nums[j]
            inv += (mid-i+1)
            j+=1
            k+=1
    # if i>len(lst1)-1:
    while(j<=r):
        temp[k] = nums[j]
        k+=1
        j+=1
    # else:
    while(i<=mid):
        temp[k] = nums[i]
        k+=1
        i+=1
    for var in range(l, r+1):
        nums[var] = temp[var]
    return inv
def merge_Sort(nums):
    temp = [0]*len(nums)
    return mergeSort(nums, temp, 0, len(nums)-1)
    
def inversionCount(arr):
    # Your Code Here
    return merge_Sort(arr)

# def inversionCount(arr, n): #!MY CODE - Time limit exceeded
    """     # Your Code Here
        rev = 0
        for i in range(n):
            for j in arr[i+1:]:
                if arr[i]>j:
                    rev+=1
        return rev """

arr = [2,4,1,3,5]
print(inversionCount(arr))