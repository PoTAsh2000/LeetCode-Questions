from solution import Solution

l1 = [2,4,3]
l2 = [5,6,4]

solution_class = Solution()

ln1 = solution_class.list_to_list_node(l1)
ln2 = solution_class.list_to_list_node(l2)
result = solution_class.addTwoNumbers(ln1, ln2)

print(result)