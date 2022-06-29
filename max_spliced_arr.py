def maximumsSplicedArray(A, B):
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