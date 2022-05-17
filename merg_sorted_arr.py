def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # i = 0 #!MY CODE
    # j = 0
    # mn = 0
    # save = 1000000
    # chk = min(m,n)
    # while(i<chk and j<chk):
    #     mn = min(nums1[i], nums2[j], save)
    #     if mn == nums1[i]:
    #         i+=1
    #     elif mn == nums2[j]:
    #         save = nums1[i]
    #         nums1[i] = mn
    #         j+=1
    # if j<n:
    #     while j<n:
    #         nums1[i] = min(nums2[j], save)
    #         if nums1[i] == save: save = 1000000
    #         else: j+=1     
    #         i+=1
    # elif i<m:
    #     while i<m:
    #         nums1[i], save = save, nums1[i]
    #         i+=1          
            
    ins = m+n-1 #!NEETCODE
    i = m-1
    j = n-1
    while i>=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[ins] = nums1[i]
            i-=1
        else:
            nums1[ins] = nums2[j]
            j-=1
        ins-=1
    #fill nums1 with leftover nums2
    while j>=0:
        nums1[ins] = nums2[j]
        j, ins = j-1, ins-1