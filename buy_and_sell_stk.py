def my_bas_stk(prices):
    Pmin = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            diff = prices[j] - prices[i]
            if(diff > 0 and diff>Pmin):
                Pmin = diff
    return Pmin

def yt_bas_stk(prices):
    op_max = 0
    i = 0
    j = 1
    while(i < len(prices) and j < len(prices)):
        if( prices[i] < prices[j]):
            pf = prices[j] - prices[i]
            op_max = max(op_max,pf)
        else:
            i = j
        j += 1
    return op_max
 

def main():
    prices = [7,1,5,3,6,4]
    op = yt_bas_stk(prices)
    print(op)
    # for k in range(len(op)):
    #     print(op[k])


if __name__ == "__main__":
    main()


