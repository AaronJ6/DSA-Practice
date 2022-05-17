def reverseBits(self, n):
    op = 0
    for i in range(32):
        op = op<<1
        bit = n%2
        op+=bit
        n=n>>1
    return op

    #!NEETCODE
    op = 0
    for i in range(32):
        bit = (n>>i) & 1
        op = op | (bit<<(31-i))
    return op