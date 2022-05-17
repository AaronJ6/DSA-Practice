from sys import last_traceback


def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    #!NEETCODE
    intervals.sort(key = lambda i: i[0])
    res = [intervals[0]]

    for start,end in intervals[1:]:
        last_end = res[-1][1]

        if start<=last_end:
            res[-1][1] = max(end, last_end)
        else:
            res.append([start,end])
    return res




    """ save = intervals[0][1] #!MY WAY
    sv_post = 0
    res = [[]]*(len(intervals))
    res[0].append(intervals[0])
    for i in range(1,len(intervals)):
        if save >= intervals[i][0]:
            j = i
            while j>0:
                del res[j]
                j-=1
            res[i].append([intervals[sv_post][0],intervals[i][1]])
            save = intervals[i][1]
        res[i].append([intervals[i][0],intervals[i][1]])
    return res """
            