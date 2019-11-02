def height(element):
    if element not in tree:
        return 0
    else:
        return 1 + height(tree[element])
 
tree = {}

if __name__ == '__main__':
	n = int(input())
	for i in range(n - 1):
	    child, parent = input().split()
	    tree[child] = parent
	 
	heights = {}
	for element in set(tree.keys()).union(set(tree.values())):
	    heights[element] = height(element)
	 
	for key, value in sorted(heights.items()):
	    print(key, value)
