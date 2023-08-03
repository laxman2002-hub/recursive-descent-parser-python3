'''This  Create Dynamic code for each function of variable '''

from read_grammar_and_remove_left_recursion import Grammar

def create_dynamic_code():
    f1 = open('execute.py','w')
    f1.write("from create_tree import Tree,pt\n\n")
    f1.write("f = open('input_string.txt','r')\n")
    f1.write("s = f.readline().strip().split()\n")
    f1.write("n = len(s)\n")
    f1.write("global p\n")
    f1.write("p = 0\n\n")
    
    for var in Grammar:
        if var[-1]=="'":
            f1.write(f'def {var[:-1]}_(par):\n')
        else:    
            f1.write("def {0}(par):\n".format(var))
        tab = 1
        f1.write('\t'*tab+f'node = Tree("{var}")\n')
        f1.write('\t'*tab+f'par.add_child(node)\n\n')
        f1.write("\t"*tab+"global p\n")
        f1.write('\t'*tab+"start = p\n\n")
        
        null_production = False

        for production in Grammar[var]:
            
            if production==['^']:
                null_production = True
                continue
            tab = 1
            f1.write("\t"*tab+"p = start\n")

            a = set()
            for sym in production:
                
                if sym[-1]=="'":
                    f1.write("\t"*tab+f'if ({sym[:-1]}_(node)):\n')
                    tab+=1
                elif sym.isupper():
                    f1.write("\t"*tab+f'if ({sym}(node)):\n')
                    tab+=1 
                else:
                    f1.write("\t"*tab+f'if p<n and "{sym}"==s[p]:\n')
                    tab+=1
                    f1.write("\t"*tab+f'node.add_child(Tree("{sym}"))\n')
                    a.add(tab)
                    f1.write("\t"*tab+"p+=1\n")

            f1.write("\t"*tab+f'return 1\n\n') 
            while tab>1:
                if tab in a:
                    f1.write("\t"*tab+'node.remove_child()\n')
                tab -= 1    

        tab = 1    
        f1.write("\t"*tab+"p = start\n")
        if null_production:
            f1.write("\t"*tab+"return 1\n")
        else:    
            f1.write("\t"*tab+'node.remove_child()\n')
            f1.write("\t"*tab+"return 0\n\n")    
    f1.write('tree = Tree("S")\n')
    f1.write('isAccepted = A1(tree)\n')

    f1.write("if isAccepted and p==n:\n")
    f1.write("\t"*1+"pt(tree)\n")
    f1.write("\t"*1+"print('\\nstring '+ ' '.join(s) +' is Accepted')\n")
    f1.write("else:\n")
    f1.write("\t"*1+"print('\\nstring '+ ' '.join(s) +' is Rejected')\n")

create_dynamic_code()
