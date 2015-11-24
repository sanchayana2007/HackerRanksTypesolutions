__author__ = 'Sanchayan'
import collections

class Node:
    def __init__(self,key,val,left = None,right = None,parent = None):
        self.key =key
        self.data = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChld(self):
        return self.right

    def isLeftChild(self):
        return self.parent.left

    def isRightChild(self):
        return self.parent.right

    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.left or self.right)
    def hasAnyChildern(self):
        return (self.left or self.right)
    def hasNoChildern(self):
        return not (self.left and self.right)
    def hasBothChilds(self):
        return (self.left and  self.right)
    def replace_Node(self):
        return NotImplementedError
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasRightChld():
                for elem in self.right:
                    yield elem


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    #***************Insertion Elements *****************#
    def insert_node(self,key,value):

        if self.root:
           self._insert_node(key,value,self.root)
        else:
            self.root = Node(key,value)
        self.size +=1

    def _insert_node(self, key, value, currentNode):
        if key > currentNode.key:
            if currentNode.hasRightChld():
                self._insert_node(self, key, value, currentNode)
            else:
                currentNode.left = Node(key,value,parent=currentNode)
                print('Enter left',key,value)
        else:
            if currentNode.hasLeftChild():
                self._insert_node(self,key,value,currentNode)
            else:
                currentNode.right = Node(key,value,parent=currentNode)
                print('Enter right ',key,value)

    def __setitem__(self, key, value):
            self.insert_node(key,value)

    #***************Getting Elements *****************#

    def get_value(self,key):
        if self.root:
            res = self._get_value(key,self.root)
            if res:

                return res.data
            else:
                return None
        else:
            return None

    def _get_value(self,key,CurrentNode):
        if not CurrentNode:
            return None
        elif CurrentNode.key == key:
            print('Current Node',CurrentNode.key,CurrentNode.data)
            return CurrentNode
        elif CurrentNode.key < key:
            if CurrentNode.hasRightChld():
                self._get_value(self,key,CurrentNode.right)
            else:
                return None

        else:
            if CurrentNode.hasLeftChild():
                self._get_value(self,key,CurrentNode.left)
            else:
                return None

    def __getitem__(self, item):
        return self.get_value(self.key)

    def __contains__(self,key):
        print('contains',key)
        if self._get_value(key,self.root):
           return True
        else:
            return False
#-------------------------------------------
    def __str__(self):
        if self.root is None:
            return None
        def display(CurrentNode):
            print('key,data',str(CurrentNode.key),str(CurrentNode.data))
            if CurrentNode.hasRightChld():
                display(CurrentNode.right)

            else:
                if CurrentNode.hasLeftChild():
                    display(CurrentNode.left)
            return str(CurrentNode.key)+ str(CurrentNode.data)
        return '\n'.join(display(self.root))





if __name__== '__main__':
    mytree = BinarySearchTree()
    mytree[1]='red'
    mytree[34]='Green'
    mytree[23]='brown'
    mytree[11]='red'
    mytree[4]='Green'
    mytree[53]='brown'
    mytree[6]='yellow'
    collections.Container.

    print(mytree)

