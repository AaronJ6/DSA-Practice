def my_dupl(nums):
    copy = set()
    for n in nums:
        if(n in copy):
            return True
        else:
            copy.add(n)
    return False

#def yt_twosum(nums):
 


def main():
    nums = [-10, -10 ,-1,-18,-19]
    op = my_dupl(nums)
    print(op)
    # for k in range(len(op)):
    #     print(op[k])


if __name__ == "__main__":
    main()


