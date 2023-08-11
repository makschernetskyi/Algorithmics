

class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.value)


compare_x = lambda value: value[0]
compare_y = lambda value: value[1]



def build_balanced_kd_tree(values, coordinate: bool = 1):

	if not values:
		return None


	values.sort(key = compare_x if coordinate else compare_y)
	values_len = len(values)
	mid = values_len//2
	head = Node(values[mid])

	head.left = build_balanced_kd_tree(values[:mid], (coordinate+1)%2)
	head.right = build_balanced_kd_tree(values[mid+1:], (coordinate+1)%2)

	return head


def store_bin_tree(head):

	nodes= [head]

	current = 0

	while current<len(nodes):

		if nodes[current]:
			nodes.append(nodes[current].left)
			nodes.append(nodes[current].right)

		current+=1

	while nodes and nodes[-1] == None:
		nodes.pop()

	return nodes





if __name__ == '__main__':

	values = [
		[1,1],
		[3,1],
		[1,2],
		[3,3],
		[-1,3],
		[-2,1],
		[-3,1],
		[-1,-1],
		[-2,-3],
		[-4,-4]
	]

	tree = build_balanced_kd_tree(values)
	print(store_bin_tree(tree))