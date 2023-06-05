def printPrevSmaller(arr, n):
    stack = []
    res = []

    for x in arr[::-1]:
        if not stack:
            res.append(-1)
        else:
            while stack and stack[0] >= x:
                stack.pop(0)
            
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[0])
        stack.insert(0,x)
    return res[::-1]

# Driver program to test insertion
# sort
arr = [1, 3, 0, 2, 5]
n = len(arr)
printPrevSmaller(arr, n)