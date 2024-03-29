def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = "" #!RECURSIVE SOLUTION
    if n==1:
        s="1"
        return s
   
    k = countAndSay(n-1)
    nn = ""
    count=1
    for i in range(len(k)):
        if i+1==len(k):
            nn+=str(count)+k[i]
        elif k[i]==k[i+1]:                        #* here checking if next element is equal then have to do count++
            count+=1
        else:
            nn += str(count)+k[i]
            count=1
    return nn

"""     c=["1"] #!ITERATIVE SOLUTION
    for i in range(n-1):
        temp=c[i]
        output=""
        count=1
        for j in range(len(temp)):
            if j+1==len(temp):
                output+=str(count)+temp[j]
                count=1
                break                    
            if temp[j]==temp[j+1]:
                count+=1
            else:
                output+=str(count)+temp[j]
                count=1
        c.append(output)
    return c[n-1] """


"""     op = "" #!MY CODE
    count = 1
    temp = n%10
    n = n//10
    while n>0:
        chk = n%10
        if chk == temp:
            count+=1
        else:
            if count>1:
                op = str(count) + str(temp) + op
            else:
                op = str(temp) + op
            temp = chk
            count = 1
        n = n//10
    if count>1:
        op = str(count) + str(temp) + op
    else:
        op = str(temp) + op
    print(op)
    return op """

n = 6
print(countAndSay(n))