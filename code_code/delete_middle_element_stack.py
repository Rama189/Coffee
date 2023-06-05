def del_mid(stack):
    if not stack:
        return
    
    length = len(stack)
    mid = length // 2 + 1
    print(mid)
    

    def dele(stack, mid):
        if len(stack) == mid:
            stack.pop()
            return
        
        val = stack.pop()
        dele(stack, mid)
        stack.append(val)
    
    dele(stack, mid)


stack = [5, 1, 0, 2, 4, 7]
# stack = [1, 2, 3]
del_mid(stack)
print(stack)