from create_tree import Tree,pt

f = open('input_string.txt','r')
s = f.readline().strip().split()
n = len(s)
global p
p = 0

def A1(par):
	node = Tree("A1")
	par.add_child(node)

	global p
	start = p

	p = start
	if (A2(node)):
		if (A3(node)):
			return 1

	p = start
	node.remove_child()
	return 0

def A2(par):
	node = Tree("A2")
	par.add_child(node)

	global p
	start = p

	p = start
	if p<n and "a"==s[p]:
		node.add_child(Tree("a"))
		p+=1
		if (A2_(node)):
			return 1

		node.remove_child()
	p = start
	node.remove_child()
	return 0

def A3(par):
	node = Tree("A3")
	par.add_child(node)

	global p
	start = p

	p = start
	if p<n and "b"==s[p]:
		node.add_child(Tree("b"))
		p+=1
		if (A3(node)):
			if p<n and "c"==s[p]:
				node.add_child(Tree("c"))
				p+=1
				return 1

				node.remove_child()
		node.remove_child()
	p = start
	return 1
def A2_(par):
	node = Tree("A2'")
	par.add_child(node)

	global p
	start = p

	p = start
	if p<n and "a"==s[p]:
		node.add_child(Tree("a"))
		p+=1
		if (A2_(node)):
			return 1

		node.remove_child()
	p = start
	return 1
tree = Tree("S")
isAccepted = A1(tree)
if isAccepted and p==n:
	pt(tree)
	print('\nstring '+ ' '.join(s) +' is Accepted')
else:
	print('\nstring '+ ' '.join(s) +' is Rejected')
