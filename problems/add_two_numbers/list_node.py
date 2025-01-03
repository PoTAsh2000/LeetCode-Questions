class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        ln_val = str(self.val)
        ln_next = str(self.next)
        print_repr = "ListNode{val: " + ln_val + ", next: " + ln_next + "}"
        return print_repr
