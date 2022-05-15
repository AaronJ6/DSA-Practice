def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    save = 100000
    i = j = 0
    while i<m and j<n:
        mn = min(nums1[i], nums2[j], save)
        if mn == nums1[i]:
            i+=1
        else:
            save = nums1[i]
            nums1[i] = mn
            i+=1
            if mn == nums2[j]: j+=1
    chk_m = m-i
    chk_n = n-j
    if chk_m >= 1:
        while chk_m >=1:
            mn = min(nums1[i],save)
            if mn == nums1[i]:
                i+=1
                chk_m-=1
            else:
                save = nums1[i]
                nums1[i] = mn
                i+=1
    elif chk_n >= 1:
        while chk_n >= 1:
            mn = min(nums2[j], save)
            if mn == save: 
                save = 100000
            nums1[i] = mn
            i+=1
            if mn == nums2[j]: 
                j+=1
                chk_n-=1
    # nums1[m+n-1] = save
    print(nums1)



nums1 = [2,0]
nums2 = [1]
merge(nums1, 1, nums2, len(nums2))
