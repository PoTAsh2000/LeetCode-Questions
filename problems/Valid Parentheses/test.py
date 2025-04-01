from solution import Solution

test_cases = {
    "()": True,
    "()[]{}": True,
    "(]": False,
    "([])": True,
    "[": False
}

solution_class = Solution()

for test_case in test_cases:
    expected_result = test_cases[test_case]
    result = solution_class.isValid(test_case)
    
    if result == expected_result:
        print(f"Successfully passed test for: '{ str(test_case) }', result was --> '{ str(result) }', expected was --> '{ str(expected_result) }'")
    else:
        print(f"Failed test for: '{ str(test_case) }', result was --> '{ str(result) }', expected was --> '{ str(expected_result) }'")