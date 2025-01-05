from solution import Solution

s = "ab"
p = ".*c"

solution_class = Solution()
result = solution_class.isMatch(s, p)
print("result -> " + str(result))