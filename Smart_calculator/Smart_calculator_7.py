import math

var_dict = {'a': 4, 'b': 5, 'c': 6, 'n': 32}
operators = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities

def is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def var_input(user_input):
    print('tomi')
    if uis[0].isalpha() == False: #not proper varibale name
        print('Invalid identifier')
    elif len(uis) == 1 and uis[0] in var_dict.keys(): #printing out the value of the existing varibale
        print(var_dict[uis[0]])
    elif len(uis) == 1 and uis[0] not in var_dict.keys(): #we can't print out the value of an unknown varibale
        print('Unknown variable')
    else: #proper varibale name
            if len(uis) == 2 or len(uis) > 3: #too few or many elements in the input
                print('Invalid assignment')
            else:
                try:
                    var_dict[uis[0]] = int(uis[2]) #define a new variable
                except ValueError:
                    if uis[2].isalpha() == False: #not proper variable name
                        print('Invalid identifier')
                    elif uis[2] in var_dict.keys(): #update an existing variable
                        var_dict[uis[0]] = var_dict[uis[2]]
                    else:
                        print('Invalid assignment')
    for i in user_input:
        if i.isalpha():
            user_input = user_input.replace(i, str(var_dict[i]))

def infix_to_postfix(user_input): #input expression
    stack = [] # initially stack empty
    postfix = '' # initially output empty
    for i in user_input:
        if i not in operators:  # if an operand then put it directly in postfix expression
            postfix+= i
        elif i=='(':  # else operators should be put in stack
            stack.append('(')
        elif i==')':
            while stack and stack[-1]!= '(':
                postfix+=stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top on higher or equal priority    
            # so pop and put in output   
            while stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]:
                postfix+=stack.pop()
            stack.append(i)
    while stack:
        postfix+=stack.pop()
    return postfix
        
def eval_postfix(postfix):
    stack = []
    postfix = postfix.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').split()
    for i in postfix:
        if i.strip() == '':
            continue 
        elif i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "-":
            op2 = stack.pop() 
            stack.append(stack.pop() - op2)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            op2 = stack.pop()
            if op2 != 0.0:
                stack.append(stack.pop() / op2)
            else:
                raise ValueError("division by zero is not allowed!")
        elif is_number(i):
                stack.append(int(i))
        else:
            raise ValueError("unknown char {0}".format(i))
    return int(stack.pop())

def smart_calc(user_input):
    if user_input.replace(' ', '') == '/exit':
        print('Bye!')
        exit()
    elif user_input.replace(' ', '') == '/help':
        print('The program calculates the sum of numbers')
    elif user_input.replace(' ', '').startswith('/'):
        print('Unknown command')
    elif user_input == '':
        None
    else:
        if len(uis) == 1 and uis[0].isalpha() == False:
            print(user_input)
        elif len(uis) == 1 or ('=' in user_input): #input variables
            var_input(user_input)
        else:
            for i in user_input:
                if i.isalpha():
                    user_input = user_input.replace(i, str(var_dict[i]))
            print(eval_postfix(infix_to_postfix(user_input)))
                          
while True:
    user_input = '33 + 20 + 11 + 49 - n - 9 + 1 - 80 + 4'
    input_list = []
    count = 0
    for i in user_input:
        if i == ' ':
            None
        elif i == '+':
            count += 1
            if count == 1:
                input_list.append(i)
        else:
            input_list.append(i)
            count = 0
    user_input = ''.join(input_list)
    input_list = []
    count = 0
    for i in range(len(user_input)):
        op = ''
        if list(user_input)[i] == ' ':
            None
        elif list(user_input)[i] == '-' and count == 0:
            count += 1
            input_list.append('-')
        elif list(user_input)[i] == '-' and count > 0 and count % 2 == 1:
            count += 1
            input_list.pop()
            input_list.append('+')
        elif list(user_input)[i] == '-' and count > 0 and count % 2 == 0:
            count += 1
            input_list.pop()
            input_list.append('-')
        else:
            input_list.append(list(user_input)[i])
            count = 0
    user_input = ''.join(input_list)
        
    count = 0
    for i in user_input:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                break
    if count != 0:
        print('Invalid expression')
        break
    elif '**' in ''.join(user_input) or '//' in ''.join(user_input) or '^^' in ''.join(user_input):
        print('Invalid expression')
        break
    elif user_input == '':
        None
    elif (user_input.isalpha() == False) and ((list(user_input)[0] == '-' and list(user_input).count('-') == 1) or ('=' not in user_input and '+' not in user_input and '*' not in user_input and '/' not in user_input and '^' not in user_input)):
        print(user_input)
        break
    else:
        if '=' in ''.join(user_input):
            uis = ''.join(user_input.split()).replace('=', ' = ').split() #treat if there are no spaces in the variable determination
        else:
            uis = ''.join(user_input.split()).replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').replace('(', ' ( ').replace(')', ' ) ').split()
            user_input = ''.join(input_list).replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').replace('(', ' ( ').replace(')', ' ) ')
        smart_calc(user_input)
        break

  

