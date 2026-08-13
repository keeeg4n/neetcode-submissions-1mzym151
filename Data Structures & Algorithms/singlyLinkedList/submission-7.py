class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    

    def get(self, index: int) -> int:
        curr = self.head

        while(index != 0):
            if curr == None:
                return -1

            if curr.next == None:
                return -1
            else:
                curr = curr.next

            index -= 1

        if curr:
            return curr.value
        else:
            return -1


    def insertHead(self, val: int) -> None:
        newNode = ListNode(value=val)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode


    def insertTail(self, val: int) -> None:
        newNode = ListNode(value=val)
        if self.head == None and self.tail == None:
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode


    def remove(self, index: int) -> bool:
        if self.head == None and self.tail == None:
            return False

        if self.head == self.tail:
            self.head == None
            self.tail == None
            return True
        
        prevNode = None
        curr = self.head
        i = 0
        while(i < index and curr):
            i += 1
            prevNode = curr
            if curr.next:
                curr = curr.next
            else:
                return False

        else:
            if curr == self.tail:
                self.tail = prevNode
            prevNode.next = curr.next
            curr.next = None
        
            return True


    def getValues(self) -> List[int]:
        curr = self.head
        values = []
        while(curr):
            values.append(curr.value)
            curr = curr.next
        
        return values

        
