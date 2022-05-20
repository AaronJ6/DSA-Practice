""" def merge_sort(arr, low, high): #!MY CODE
    if low == high:
        return
    mid = (low + high)/2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge_arr(arr, low, high)

def merge_arr(arr, low, high):
    mid = (low + high)/2
    i = low
    j = mid+1
    k = low
    temp = [0] * (high - low + 1)
    while (i<= mid and j<high):
        if(arr[i]<arr[j]):
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            k+=1
            j+=1
    for x in range(low,high+1):
        arr[x] = temp[x] """

    # MERGE_SORT #!WORKING
def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)
    return result

def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst 