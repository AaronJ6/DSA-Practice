def my_twosum(nums, target):
    op = []
    for i in range(len(nums)):
        if(len(op) < 2):
            a = target - nums[i]
            j = i+1
            if(a == 0):
                op.append(i)
                print(op[0])
                quit
            if(a != 0):
                while(j<len(nums) and a != 0 and len(op) != 2 ):
                    if (nums[j] == a):
                        op.append(i)
                        op.append(j)
                        a += nums[i]
                        a = target - a
                    j += 1
        else:
            break
    for k in range(len(op)):
        print(op[k])
    return op

def yt_twosum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        if (target - n) in hashmap:
            return(hashmap[target-n], i)
        hashmap[n] = i  


def main():
    nums = [-10,-1,-18,-19]
    target = -19
    op = my_twosum(nums, target)
    # for k in range(len(op)):
    #     print(op[k])


if __name__ == "__main__":
    main()


