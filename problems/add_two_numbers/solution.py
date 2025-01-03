from list_node import ListNode

class Solution(object):
    def __init__(self):
        pass
    
    def addTwoNumbers(self, ln1, ln2):
        # convert list node to list for easier processing
        arr1 = self.list_node_to_list(ln1)
        arr2 = self.list_node_to_list(ln2)

        # reverse both lists
        reversed_arr1 = self.reverse_list(arr1)
        reversed_arr2 = self.reverse_list(arr2)
        
        # concat the values in the reversed arrays to a string of numbers
        value1 = ''.join(map(str, reversed_arr1))
        value2 = ''.join(map(str, reversed_arr2))
        # parse the string values to integers and sum them, then make the sum a string
        sum = int(value1) + int(value2)
        sum = str(sum)
        
        result = self.sum_to_int_array(sum) # loop each char of the sum string and add each char to a new int array
        result = self.reverse_list(result) # reverse the int array
        result = self.list_to_list_node(result) # convert the list to a list node and return te result
        return result

    def sum_to_int_array(self, sum):
        intArr = []
        for char in sum:
            intArr.append(int(char))
        return intArr
       
    def reverse_list(self, arr):
        new_list = []
        for item in reversed(arr):
            new_list.append(item)
        return new_list
    
    def list_to_list_node(self, arr):
        if len(arr) < 1:
            return None

        arr_value = arr[0]
        if len(arr) == 1:
            return ListNode(arr_value)
        return ListNode(arr_value, next=self.list_to_list_node(arr[1:]))
    
    def list_node_to_list(self, ln):
        new_list = []
        while True:
            new_list.append(ln.val)
            if ln.next == None:
                break
            ln = ln.next
        return new_list