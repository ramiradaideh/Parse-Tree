def precedence(oper):
    if oper in ['+', '-']:
        return 1
    else:
        return 2

def operatorp(x):
    return x in ['+', '-', '/', '*']
def numberp(x):
    return not operatorp(x)

def parse(expr):
    return parseHelper(expr, [], [])


#all of these functions are from the textbook 



def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    #this if statement checks if the list contains another list in it
    if isinstance(expr[0],list):
        return Paranthesis(expr,operators,operands) 
    #this checks if the elemnt in the list contains a factorial 
    if expr[0] == "!":
        return Factorial(expr,operators,operands)
    
    if numberp(expr[0]): 
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    
    if operators == [] or precedence(expr[0]) > precedence(operators[0]): 
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    
    else:
        return handleOp(expr, operators, operands)
    #regular expression from the textbook 
    #this function will evaluate the inner list and then add it back into the opearnds 
def Paranthesis(expr,operators,operands):
    result = parseHelper(expr[0],[],[])
    return parseHelper(expr[1:],operators,[result]+operands)

    #this will operate on the factorial sign by placing in its own tree and containing only one element
def Factorial(expr,operators,operands):
    return parseHelper(expr[1:],operators,[['!',operands[0],[]]] + operands[1:])

def handleOp(expr, operators, operands):
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:]) 
    
#x=[['4', '+', '3' ,'!'], '*', '7']	
x=['4' , '/' ,['7', '+' ,'2']]
#x=[['4'], '+', ['3'], '+', '6']
#x="( 4 + 3 * 7 - 5 / ( 3 + 4 ) + 6 )"
#    [ 3.4, 24.8, 8.0, -6, 22 ] and [ 99, 107 ]: 
#    5 3.4 24.8 8.0 -6 22

print("--", parse(x))