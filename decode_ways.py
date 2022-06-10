def rec_fn(i, s):
    if i >= len(s):
        return 0
    else:
        lng1, lng2 = 0, 0
        num1 = int(s[i])
        if i+1<len(s):
            num2 = int(s[i])
            num2 = num2*10 + int(s[i+1])
        else:
            num2 = 0
        if num1>0 and num1<27:
            lng1 = 1+rec_fn(i+1,s)
        if num2>0 and num2<27:
            lng2 = 1+rec_fn(i+2,s)
        return max(lng1, lng2)

s = "2206"
print(rec_fn(0,s))