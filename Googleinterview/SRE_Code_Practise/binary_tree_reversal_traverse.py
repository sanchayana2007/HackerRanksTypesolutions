from inspect import stack
from signal import pthread_kill

class Node:
    def __init__(self,val= None):
        self.left = None 
        self.right = None
        self.data = val

class Bst:
    def __init__(self,val= None) -> None:
        self.stack = []
        self.count =0 
        pass
        
    def insertR(self,node = None, data= None):
       
        if node is None:
            self.count +=1
            return Node(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insertR(node.left, data)
        elif data > node.data:
            node.right = self.insertR(node.right, data)
        #print(node.data)
        return node

    def dfs(self,root):
        print("###DFS##########")
        self.stack.append(root)
        while len(self.stack) > 0:
            curr = self.stack.pop()
            print(curr.data)
            if curr.left :
                self.stack.append(curr.left)
            if curr.right:
                self.stack.append(curr.right)
            

    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node
    
    def display(self,root):
        print('######## DISPLAY ################')
        lines, *_ = self._display_aux(root)
        for line in lines:
            print(line)

    def _display_aux(self,root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        curr = root
        if curr.right is None and curr.left is None:
            line = '%s' % curr.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if curr.right is None:
            lines, n, p, x = self._display_aux(curr.left)
            s = '%s' % curr.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if curr.left is None:
            lines, n, p, x = self._display_aux(curr.right)
            s = '%s' % curr.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(curr.left)
        right, m, q, y = self._display_aux(curr.right)
        s = '%s' % curr.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)


    def traverseIdPostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """

        if root is not None:
            print(root.data)
            self.traverseIdPostorder(root.left)
            
            self.traverseIdPostorder(root.right)
            
    
if __name__ == "__main__":
    a= [1,34,321,143,58]
    
    t=Bst()
    root = t.insertR(None,1)
    for i in a:
        t.insertR(root,i)
    print("Traverse Inorder")
    
    t.traverseInorder(root)
   
    #t.traverseIdPostorder(root)
   
    t.dfs(root)
    #print(t.stack)
    t.display(root)
    t.traverseIdPostorder(root)
   