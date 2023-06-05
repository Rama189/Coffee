def rev(stack):
    if len(stack) == 0:
        return

    val = stack.pop()
    rev(stack)
    
    def ins(stack,val):
        if len(stack) == 0:
            return stack.append(val)
        
        temp = stack.pop()
        ins(stack,val)
        stack.append(temp)
    
    ins(stack,val)


stack = [1, 2, 3]
rev(stack)
print(stack)