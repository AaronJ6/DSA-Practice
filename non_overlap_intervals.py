def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort()
    op=0
    last = intervals[0][1]

    for start,end in intervals[1:]:
        if start<last:
            op+=1
            last = min(end,last)
        else:
            last = end
    return op