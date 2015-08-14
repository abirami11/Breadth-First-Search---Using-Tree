import Queue
class TreeNode:
	def __init__(self, key, left=None,right=None,parent = None):
		self.leftChild = left
		self.rightChild = right
		self.keyValue = key
		self.parent = parent

	def binary_insert(self,key):
		if self.keyValue:
			if key <= self.keyValue :
				if self.hasleftChild() :
					self.leftChild.binary_insert(key)
				else:
					self.leftChild = TreeNode(key)
			else:
				if self.hasRightChild():
					self.rightChild.binary_insert(key)
				else:
					self.rightChild = TreeNode(key)
		else:
			self = TreeNode(key)


	def bfs(self):
		thisLevel = [self] 
		while thisLevel:
			next = []
			for n in thisLevel:
				print n.keyValue
				if n.leftChild:
					next.append(n.leftChild)
				if n.rightChild:
					next.append(n.rightChild)
			thisLevel = next
			

node = TreeNode(10)
node.binary_insert(8)
node.binary_insert(13)
node.binary_insert(9)
node.binary_insert(12)
node.binary_insert(15)
node.binary_insert(7)
#node.display_tree()
node.bfs()
