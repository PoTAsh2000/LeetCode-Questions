from solution import Solution

class Test(object):
    def test(self, digits, expected):
        solution = Solution()
        
        result = solution.plusOne(digits)

        if result == expected:
            return f"test success -> test array: {str(digits)} result: {result} expected: {expected}"
        return f"test failed -> test array: {str(digits)} result: {result} expected: {expected}"
    

test = Test()
print(test.test([1,2,3], [1,2,4]))
print(test.test([4, 3, 2, 1], [4,3,2,2]))
print(test.test([9], [1,0]))