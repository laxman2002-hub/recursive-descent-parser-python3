''' Reading Grammar from File '''

f = open('input_grammar.txt','r')
Grammar = {}
start = 'S'
k = 0
variables = []
lines = []

total_production = int(f.readline())
for i in range(total_production):
    line = f.readline()
    lines.append(line)
    production = line.split('->')
    left = production[0].strip()
    variables.append(left)
    if k==0:
        start = left
        k = 1
    right = production[1].strip() # A -> B
    right = right.split('|')
    Grammar[left] = []
    for pro in right:
        Grammar[left].append(pro.strip().split())

# print(Grammar)
# print(variables)
''' Renaming of Grammar Variables'''

rename = {}
p = 1
for e in Grammar:
    rename[e] = 'A'+str(p)
    p+=1
# print(rename)

''' Create new Grammar with new variables naming '''

new_Grammar = {}
for each_var in Grammar:
    new_var = rename[each_var]
    new_Grammar[new_var] = []
    for each_production in Grammar[each_var]:
        new = []
        for sym in each_production:
            if sym.isupper():
                if sym not in rename:
                    print("Please give the production for grammer variable :",sym)
                    exit(0)
                new.append(rename[sym])
            else:
                new.append(sym)
        new_Grammar[new_var].append(new)     

 
m = p


def Remove_Immediate_Left_Recusion(new_Grammar,Var):
    # eg :  A -> Aa1 | Aa2 | b1 | b2 | ^
    with_left_recur = []        # [a1 , a2]
    without_left_recur = []     # [b1 , b2]
    for each_production in new_Grammar[Var]:
        if each_production[0]==Var:
            with_left_recur.append(each_production[1:])
        else:
            without_left_recur.append(each_production)

    if with_left_recur:  # if left recusion exist
        new_Grammar[Var] = []
        new = Var+str("'")
    
        for each_production in without_left_recur:
            if each_production==['^']:
                new_Grammar[Var].append([new])   # A -> A'
            else:    
                new_Grammar[Var].append(each_production+[new])  # A -> b1A' | b2A'

        new_Grammar[new] = []    
        for each_production in with_left_recur:
            new_Grammar[new].append(each_production+[new])  # A' -> a1A' | a2A'
        new_Grammar[new].append(['^'])

def Remove_left_Recursion(new_Grammar):

    Remove_Immediate_Left_Recusion(new_Grammar,'A1')
    for i in range(2,m):
        Var = 'A'+str(i)

        for j in range(1,i):
            new = 'A'+str(j)
            length = len(new_Grammar[Var])

            for k in range(length):
                production = new_Grammar[Var][k]
                start = production[0]
                if start==new:
                    left = new_Grammar[Var][:k]
                    right = new_Grammar[Var][k+1:]
                    post = production[1:]

                    replace = []
                    for pro in new_Grammar[start]:
                        if pro==['^']:
                            replace.append(post)
                        else:    
                            replace.append(pro+post)

                    new_Grammar[Var] = left+replace+right 
                    
        Remove_Immediate_Left_Recusion(new_Grammar,Var)   


''' Removing left recursion from the Grammar~~~~~~~~~~~~~~~~~~~~~~~'''

Remove_left_Recursion(new_Grammar) 
print("Given grammar is  ~\n")
for each in lines:
    print(each)

print("\nWe rename Grammar variables as ~\n")
for each in rename:
    print(each+" = "+rename[each]+'\n')

print('\n\nAfter removing Left recursion(if exist) new renamed Grammar is ~ \n')
print("S -> A1\n")
for var in new_Grammar:
    pro = var+" -> "
    for each in new_Grammar[var]:
        for sym in each:
            pro+=sym+' '
        pro+='| '
    print(pro[:-3]+'\n')        

Grammar = new_Grammar