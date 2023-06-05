def rec_sort(stack):
    if not stack:
        return

    val = stack.pop()
    rec_sort(stack)

    def insert(stack, val):
        #Base condition
        if not stack or stack[-1] >= val:
            return stack.append(val)
        
        #Hypothesis
        v = stack.pop()
        insert(stack, val)

        #Induction 
        stack.append(v)

    #Induction - Here again we're calling recursive function to insert instead of using loop.
    insert(stack, val)

# stack = [2, 3, 9, 5] 
stack = [5, 1, 0, 2]
rec_sort(stack)
print(stack)