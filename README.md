# recursive-descent-parser-python3 (With Parser Tree)
recursive descent parser which take a CFG as input and generate dynamic code which validate a input string belong to CFG or not with showing its Parsar Tree. . then take a input string and check that string is belongs to CFG or not .

install python module PrettyPrint with command ~

```-> pip install print_tree```

first write your CFG in input_grammar.txt file (first line is number of product rules in grammar and the following lines are rules(keep maintain require syntax of input rules))
then write the required string which we want to check in input_string.txt file

run these command in terminal with correct directory ~

```-> python3 create_dynamic_code.py```

![image](https://github.com/laxman2002-hub/recursive-descent-parser-python3/assets/81050546/a85d13b3-6739-442e-9e87-b7df94ec9cc5)

```-> python3 execute.py``` 

and see the output of code in the console(terminal)
![image](https://github.com/laxman2002-hub/recursive-descent-parser-python3/assets/81050546/0b1400f4-3b9e-49a8-aa0c-ccb1ce065ad0)

if (string is Accepted) -> then there is a parser tree print in the console for input string 
else -> output as Rejected
