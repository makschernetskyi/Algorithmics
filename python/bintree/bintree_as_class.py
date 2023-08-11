


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return str(self.value)

def print_bin_tree(head):
	nodes_to_print = [head]

	current = 0

	while current<len(nodes_to_print):

		if nodes_to_print[current].left:
			nodes_to_print.append(nodes_to_print[current].left)
		if nodes_to_print[current].right:
			nodes_to_print.append(nodes_to_print[current].right)

		current+=1

	print(nodes_to_print)








if __name__ == '__main__':



	bin_tree_head = Node(4)
	bin_tree_head.left = Node(2)
	bin_tree_head.left.left = Node(1)
	bin_tree_head.left.right = Node(3)
	bin_tree_head.right = Node(6)
	bin_tree_head.right.left = Node(5)
	bin_tree_head.right.right = Node(7)

	print_bin_tree(bin_tree_head)

