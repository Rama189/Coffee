#User function Template for python3
import math
class Solution:
    def NBitBinary(self, N):
        # code here
        # print(math.ceil(N/2))
        # mid = math.ceil(N/2)
        def get_bin(n, one, zero, sol):
            if n == 0:
                print(sol)
                return
            
            sol1 = sol + "1"
            get_bin(n - 1, one + 1, zero, sol1)

            if one > zero:
                sol2 = sol + "0"
                get_bin(n - 1, one, zero + 1, sol2)    
                
        get_bin(N,0, 0,  "")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=1
    for i in range(T):
        n = 3
        ob = Solution()	
        answer = ob.NBitBinary(n)
        # for value in answer:
        #     print(value,end=" ")
        # print()


# } Driver Code Ends