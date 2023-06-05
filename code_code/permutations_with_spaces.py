#User function Template for python3

class Solution:
    def permutation (self, s):

        def p_perm(s, res):
            if len(s) == 0:
                print(res)
                return

            sol1 = res + " " + s[0]
            p_perm(s[1:], sol1)

            sol2 = res + s[0]
            p_perm(s[1:], sol2)
        
        p_perm(s[1:], s[0])

if __name__ == '__main__': 
    ob = Solution()
    t = 1
    for _ in range (t):
        S = "abc"
        ans = ob.permutation(S)
        # write = ""
        # for i in ans:
        #     write += "(" + i + ")"
        # print(write)