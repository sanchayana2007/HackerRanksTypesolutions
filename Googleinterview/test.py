class Node():
	def __init__(self, d):
		self.left = None
		self.right = None
		self.val = d

def tree_insert(root,data):
	
	if root == None:
		root = Node(data)	
	elif data == root.val:
		return root
	#Insert data in right as right as root
	elif data > root.val:
		root.right = tree_insert(root.right,data)
	#Insert data in left as left as root	
	elif data < root.val:
		root.left = tree_insert(root.left, data)
	else:
		pass 
	return root

def tree_insertNR(root,data):
	
	if root == None:
		root = Node(data)	
	elif data == root.val:
		return root
	#Insert data in right as right as root
	elif data > root.val:
		new_root = root.right

		while new_root != None:
			if  data > new_root.val:
				print("reachedNode",new_root.val)
				new_root=  new_root.right

			elif  data < new_root.val:
				print("reachedNode",new_root.val)
				new_root=  new_root.left
			elif data ==  new_root.val:
				return root    
		new_root = Node(data)
	elif data < root.val:
		new_root = root.left
		while new_root != None:
			if  data > new_root.val:
				print("reachedNode",new_root.val)
				new_root=  new_root.right
			elif  data < new_root.val:
				print("reachedNode",new_root.val)
				new_root=  new_root.left
			elif data ==  new_root.val:
				return root
		new_root= Node(data)	
	else:
		pass 
	return root


def inorderNR(root):
	temp = root
	stack = []
	stack.append(root)
	while len(stack) > 0 :
		temp = stack.pop()
		print(temp.val)

		if temp.right is not None:
			stack.append(temp.right)
		elif temp.left is not None:
			stack.append(temp.left)

		else:
			break

def Height(root):
	temp = root
	stack = []
	stack.append(root)
	lht = 0 
	rht = 0 
	while len(stack) > 0:
		temp=stack.pop()
		if temp.right is not None:
			
			rht +=1
			stack.append(temp.right)
		elif temp.left is not None:
			stack.append(temp.left)
			lht+=1
		else:
			break
	print(max(lht,rht)+1 )

def preorderNR(root):
	temp = root
	stack = []
	while True:
		#If the node is present 
	    if temp is not None:
		    stack.append(temp)
			#Move to left 1st as its inorder 
		    temp = temp.left
		##we rach the end of left 
	    elif(stack):
		    temp = stack.pop()
		    print(temp.val)
		    temp = temp.right 
			
	    else:
		    break





	# A funtion to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
 

# Function to find a pair in an array with a given sum using hashing
if __name__=="__main__":
        
    root = Node(1)
    tree_insert(root, 2)
    tree_insert(root, 4)
    tree_insert(root, 3)
    tree_insert(root,5)
    tree_insert(root,78)
    tree_insert(root,15)
    tree_insert(root,11)
    tree_insert(root,7)
    tree_insert(root,6)


    tree_insertNR(root,452) 

	#Tree height
    Height(root)
    printInorder(root)
    #inorderNR(root)
