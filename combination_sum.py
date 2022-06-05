def combinationSum(candidates, target):
    op = []        
    def dfs(i, res, total):
        if total == target:
            op.append(res.copy())
            return
        if i>=len(candidates) or total>target:
            return
        
        res.append(candidates[i])
        dfs(i,res,total+candidates[i])
        res.pop()
        dfs(i+1,res,total)
    
    dfs(0,[],0)
    return(op)