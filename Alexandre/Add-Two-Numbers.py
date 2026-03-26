class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        add = 0

        while l1 or l2 or add:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            soma = val1 + val2 + add
            add = soma // 10

            current.next = ListNode(soma % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next    

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Criar l1: 2 -> 4 -> 3
#l1 = ListNode(2, ListNode(4, ListNode(3)))
# Criar l2: 5 -> 6 -> 4
#l2 = ListNode(5, ListNode(6, ListNode(4)))

#segundo exemplo do desafio
#l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
#l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

# criar lista numeros negativos
l1 = ListNode(-2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(-6, ListNode(4)))

#print("Desafio proposto pelo LeetCode: https://leetcode.com/problems/add-two-numbers/")
#print("output esperado: [7, 0, 8]")
#print("output obtido: ", to_list(Solution().addTwoNumbers(l1, l2)))

print("Teste com numeros negativos: ")
print("l1: ", to_list(l1))
print("l2: ", to_list(l2))
print("Resultado: ", to_list(Solution().addTwoNumbers(l1, l2)))