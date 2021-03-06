'''perform following function
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.start = None

    def print(self):
        if self.start is None:
            print("Linked list is empty")
            return
        itr = self.start
        llstr = ''
        while itr!=None:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.start
        while itr!=None:
            count+=1
            itr = itr.next
        print(count,end=' ')
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.start)
        self.start = node

    def insert_at_end(self, data):
        if self.start is None:
            self.start = Node(data, None)
            return

        itr = self.start

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_after_value(self, data_after, data_to_insert):
        if self.start is None:
            print('empty')
        else:
            itr=self.start
            while itr.data!=data_after:

                itr=itr.next
            else:
                node=Node(data_to_insert,itr.next)
                itr.next=node

    def remove_by_value(self, data):
        itr=self.start
        while itr.next!=None:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(17)
    ll.insert_at_end(18)
    ll.insert_at_end(34)
    ll.insert_at_end(23)
    ll.insert_at_end(84)
    ll.insert_at_end(92)
    ll.insert_at_end(41)
    ll.insert_at_end(81)
    ll.insert_at_end(29)
    ll.insert_at_end(43)
    ll.insert_at_end(39)
    ll.insert_after_value(92,72)
    ll.insert_after_value(72,16)
    ll.print()
    ll.remove_by_value(16)
    ll.print()