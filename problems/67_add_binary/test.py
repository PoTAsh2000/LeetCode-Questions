from solution import Solution

def test (a, b, expected):
    solution = Solution()
    result = solution.addBinary(a, b)
    
    if result == expected:
        return f"test success -> a: {a}, b: {b}, result: {result}, expected: {expected}"
    return f"test failed -> a: {a}, b: {b}, result: {result}, expected: {expected}"

print(test("11", "1", "100"))
print(test("1010", "1011", "10101"))
print(test("0", "0", "0"))