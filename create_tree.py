from PrettyPrint import PrettyPrintTree
from colorama import Back

class Tree:
    def __init__(self, value):
        self.val = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child
    def remove_child(self):
	    self.children.pop()
	    
pt = PrettyPrintTree(lambda x: x.children, lambda x: x.val ,color=Back.RED)