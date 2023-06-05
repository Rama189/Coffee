def printPrevGreater(arr,n):
    stack = []
    res = []

    for x in arr:
        if not stack:
            res.append(-1)
        else:
            while stack and stack[0] <= x:
                stack.pop(0)
            
            if stack:
                res.append(stack[0])
            else:
                res.append(-1)
        
        stack.insert(0,x)
    return res


# Driver code
arr = [ 10, 5, 11, 10, 20, 12 ]
n = len(arr)
printPrevGreater(arr, n)