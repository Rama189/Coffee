#Sorting using recursion
#Check this vid https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=7

def rec_sort(l):
    #Base condition
    if not l:
        return
    
    val = l[-1]
    l.pop()

    #Hypothesis
    rec_sort(l)
    
    def insert(l, val):
        #Base condition
        if not l or l[-1] <= val:
            return l.append(val)
        
        #Hypothesis
        v = l.pop()
        insert(l, val)

        #Induction 
        l.append(v)

    #Induction - Here again we're calling recursive function to insert instead of using loop.
    insert(l, val)

l = [0,2,1,9,6,8,5]
l = [0,2,1,6,8,5,1]
rec_sort(l)
print(l)




#####Below is the function if you wanted the result in other array
# def rec_sort(l, res):
#     if not l:
#         return []
    
#     rec_sort(l[:-1], res)
#     val = l[-1]

#     def insert(res, val):
#         if not res or res[-1] <= val:
#             return res.append(val)
        
#         v = res.pop()
#         insert(res, val)
#         res.append(v)

#     insert(res, val) 
#     return res

# l = [0,2,1,9,6,8,5]
# res = []
# rec_sort(l, res)
# print(res)