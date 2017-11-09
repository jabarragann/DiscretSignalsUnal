# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal

"""
class Node(object):
        def __init__(self, data=None, next_node=None, previous_node=None):
            self.data = data
            self.next_node = next_node
            self.previous_node=previous_node
    
        def get_data(self):
            return self.data
    
        def get_next(self):
            return self.next_node
        
        def get_previous(self):
            return self.previous_node
    
        def set_next(self, new_next):
            self.next_node = new_next
            
        def set_previous(self,new_previous):
            self.previous_node=new_previous
            

class myLinkedList():
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.size=0
        self.head.set_next(self.tail)                
        self.tail.set_previous(self.head)
                        
    def insertAfterHead(self,data):
        dataNode=Node(data)
        
        #four connections are need to insert a node
        dataNode.set_next(self.head.get_next())
        dataNode.set_previous(self.head)
        self.head.get_next().set_previous(dataNode)
        self.head.set_next(dataNode)
        self.size+=1
    
    def insertBeforeTail(self,data):
        dataNode=Node(data)
        
        #four connections are need to insert a node
        dataNode.set_previous(self.tail.get_previous())
        dataNode.set_next(self.tail)
        self.tail.get_previous().set_next(dataNode)
        self.tail.set_previous(dataNode)
        self.size+=1
    
    def zeros(self,size):
        for i in range(size):
            self.insertAfterHead(0)
            
    def toString(self):
        arr=[]
        arr.append("H")
        movingNode=self.head.get_next()
    
        while movingNode.get_next() is not None:
            arr.append(movingNode.get_data())
            movingNode=movingNode.get_next()    
        arr.append("T")
        
        print(arr)
        
    def toArray(self):
        arr=[]
        movingNode=self.head.get_next()
    
        while movingNode.get_next() is not None:
            arr.append(movingNode.get_data())
            movingNode=movingNode.get_next()    
        
        return arr
        
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    
    def removeFromHead(self,N):
        if self.size>N:
            tempNode1=self.head.get_next()
            for i in range(N):
                tempNode1=tempNode1.get_next()
            
            self.head.set_next(tempNode1)
            tempNode1.set_previous(self.head)
            self.size-=1
                
if __name__=="__main__":
    x = [i*3 for i in range(5)]
    
    myLinked=myLinkedList()
    
    for i in x:
    #    myLinked.insertBeforeTail(i)    
        myLinked.insertAfterHead(i)
    
    movingNode=myLinked.getHead().get_next()
    
    while movingNode.get_next() is not None:
        print(movingNode.get_data())
        movingNode=movingNode.get_next() 
        
        
    myLinked.toString()