def simplified_maximumsSplicedArray(A, B): #!Simplified code of the below this function 
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    def kadane(A, B):
        res = cur = 0
        for i in range(len(A)):
            cur = max(0, cur + A[i] - B[i])
            res = max(res, cur)
        return res + sum(B)
    return max(kadane(A, B), kadane(B, A)) 

# def maximumsSplicedArray(nums1, nums2): #!Kadane's Algo
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: int
#     """
#     sum1 = sum(nums1)
#     sum2 = sum(nums2)
    
#     ans = max(sum1, sum2)
    
#     chk1=chk2=max1=max2 = 0
    #? Algo loop
#     for i in range(len(nums1)):
#         chk1 += (nums2[i]-nums1[i])
#         chk2 += (nums1[i]-nums2[i])
        
#         max1 = max(max1, chk1)
#         max2 = max(max2, chk2)
        
#         if chk1<0:
#             chk1 = 0
#         if chk2<0:
#             chk2 = 0
    
#     ans = max(ans, sum1+max1, sum2+max2)
    
#     return ans