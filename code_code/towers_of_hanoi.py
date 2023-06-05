# User function Template for python3

class Solution:
    def __init__(self):
        self.count=0

    def toh(self, N, fromm, to, aux):
        if N == 0:
            return self.count
        
        self.toh(N - 1, fromm, aux, to)
        print("move disk {} from rod {} to rod {}".format(N, fromm, to))
        self.count += 1
        self.toh(N - 1, aux, to, fromm)

        return self.count

import math
def main():
    T = 1

    while(T > 0):
        N = 3
        ob = Solution()
        print(ob.toh(N, "A", "C", "B"))
        T -= 1

if __name__ == "__main__":
    main()