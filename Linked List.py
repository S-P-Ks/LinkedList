class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
    def insert_values(self,dataList):
        for data in dataList:
            self.insert_at_end(data)
            
    def getCount(self):
        count = 0
        itr = self.head
        
        while itr.next:
            count+1
            itr = itr.next
        
        return count
            
    def remove(self,index):
        if index < 0 or index > self.getCount():
            print("The index is out of Bound")
    
    def show(self):
        if self.head is None:
            print("The Linked List is empty")
            return
         
        itr = self.head
        litr = ""
        
        while itr:
            litr += str(itr.data) + "-->"
            itr = itr.next
            
        print(litr)
        
li = LinkedList()
li.insert_at_beginning(5)
li.insert_at_beginning(15)
li.insert_at_beginning(75)
li.insert_at_end(25)
li.insert_at_end(50)
li.insert_at_end(55)
li.insert_values(['Apple','Banana','Grapes','PineApple'])

li.remove(12)
li.show()