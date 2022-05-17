n = 43261596

op = 0
arr = []
while n!=0:
    arr.append(n%2)
    n = n//2
i = 0
while len(arr)!=0:
    ad = arr.pop()
    if ad == 1:
        op+=pow(2,i)
    i+=1
print(op)