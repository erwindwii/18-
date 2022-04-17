from operator import truediv
from os import curdir
from pickletools import read_uint1
import re
from turtle import left
from xml.dom.minidom import Element


class binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None #left side
        self.right = None #right side
    
    def add_child(self, data):
        if data == self.data: #check data
            return
        
        if data < self.data:
            #add data in left subtree
            if self.left: #check left have some value
                self.left.add_child(data) #use pass to check
            else: #if left node empty 
                self.left = binarytree(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarytree(data)
        
    
    def in_order_traversal(self):
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        #visit base node
        elements.append(self.data)
        
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        Elements = []

        if self.left:
            Elements += self.left.post_order_traversal()
        if self.right:
            Elements += self.right.post_order_traversal()
        
        Elements.append(self.data)

        return Elements

    def pre_order_traversal(self):
        Elements = [self.data]

        if self.left:
            Elements += self.left.pre_order_traversal()
        if self.right:
            Elements += self.right.pre_order_traversal()
        return Elements
        
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False            #val might be in left subtree
                                        #if self.left:#check
                                        #pass
        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()
    def finMin(self):
        if self.left is None:
            return self.data
        return self.left.finMin()

def build_tree(elements):
    root = binarytree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = []
    numbers_tree = build_tree(numbers)
    #print(numbers_tree.in_order_traversal())# traversal in order
    #print(numbers_tree.search(20)) #search value node
    #print('max number tree is', numbers_tree.findMax())
    #print('min number tree is', numbers_tree.finMin())
    #print('post order traversal', numbers_tree.post_order_traversal())
    #print('pre order traversal', numbers_tree.pre_order_traversal())


    
