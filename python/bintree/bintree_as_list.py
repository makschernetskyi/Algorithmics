

bintree = [4, 2, 6, 1, 3, 5, 7]


def search_in_bin_tree(tree, element):

	tree_len = len(tree)
	lvl_coefficient = 1
	index = 0
	while index<tree_len:
		if element == tree[index]:
			return True
		elif element > tree[index]:
			index= index +lvl_coefficient + (index+1)%lvl_coefficient+1
		else:
			index= index +lvl_coefficient + (index+1)%lvl_coefficient
		lvl_coefficient*=2
	return False

def append_to_bin_tree(tree, element):

	tree_len = len(tree)
	lvl_coefficient = 1
	index = 0

	#print('enter', f"{index = }", f"{tree_len = }")
	while index<tree_len:
		if element == tree[index]:
			#print('match', f"{bintree[index] = }", f"{element = }")
			return
		elif element > tree[index]:
			index= index +lvl_coefficient + (index+1)%lvl_coefficient + 1
			#print('greater')
		else:
			index= index +lvl_coefficient + (index+1)%lvl_coefficient
			#print('less')
		lvl_coefficient*=2
		#print(index)
	#print(index)
	tree.extend([None]*(index - tree_len) + [element])
	return


if __name__ == '__main__':
	new_bintree = []
	elements_to_add = [1,4,2,5,8,0,9,7]
	for e in elements_to_add[:3]:
		append_to_bin_tree(new_bintree,e)
		#print(new_bintree)
	print(new_bintree)