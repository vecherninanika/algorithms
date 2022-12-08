class Solution(object):
    def getDecimalValue(self, head):
        """Сложность: O(n).

        Args:
            head (ListNode): a reference node to a singly-linked list

        Returns:
            int: decimal value of the number in the linked list
            """
        string = ''
        while head:
            string += str(head.val)  #добавляем к строке значение узла в формате str
            head = head.next  # меняет значение head - теперь это следующий узел
        return int(string, 2)   

# int(object, основание системы счисления) - 
# преобразует object к целому числу в десятичной системе счисления
