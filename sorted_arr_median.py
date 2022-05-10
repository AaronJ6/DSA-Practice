def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    A,B = nums1, nums2
    
    total = len(nums1) + len(nums2)
    half = total//2
    
    if len(B)<len(A): A, B = B, A
    
    #Time complexity = O(log(min(n,m))) since we are doing binary search on the smaller array
    l, r = 0, len(A) - 1
    while True:
        m1 = (l+r)//2
        m2 = half - m1 - 2
        
        Aleft = A[m1] if m1>=0 else float("-infinity")
        Aright = A[m1+1] if (m1+1)<len(A) else float("infinity")
        
        Bleft = B[m2] if m2>=0 else float("-infinity")
        Bright = A[m2+1] if (m2+1)<len(B) else float("infinity") 
        
        if Aleft <= Bright and Bleft <= Aright: #correct partition
            if total % 2:
                return( min(Aright,Bright) )
            else:
                return ( (max(Aleft, Bleft)+min(Aright,Bright)) / 2)
        elif Aleft > Bright:
            r = m1 - 1
        else:
            l = m1 + 1