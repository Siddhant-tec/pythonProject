class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self):
        A = list(map(int, input().rstrip().split()))
        #B = []
        result = 0
        for numbers in A:
            count = 0
            while numbers < len(A) and A[numbers] > 0:
                count += 1
                numbers += 1

            result = max(result, count)
        print(result)               




sol = Solution()
sol.maxset()
