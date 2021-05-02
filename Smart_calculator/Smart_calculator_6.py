# write your code here
import math

def var_input(user_input):
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


def calc(user_input):
    numbers1 = uis
    numbers2 = []
    for i in range(len(numbers1)):
        if i % 2 == 1 and numbers1[i].count('+') != len(numbers1[i]) and numbers1[i].count('-') != len(numbers1[i]):
            print('Invalid expression')
            numbers2 = []
            break
        elif i % 2 == 1 and numbers1[i].count('+') == len(numbers1[i]):
            numbers2.append(1)
        elif i % 2 == 1 and numbers1[i].count('-') == len(numbers1[i]):
            numbers2.append(int(math.pow(-1, numbers1[i].count('-'))))
        elif i % 2 == 0:
            try:
                if numbers1[i] in var_dict.keys():
                    numbers2.append(var_dict[numbers1[i]])
                else:    
                    numbers2.append(int(numbers1[i]))
            except ValueError:
                print('Invalid expression')
                numbers2 = []
                break
    numbers3 = []
    for i in range(len(numbers2)):
        if i == 0:
            numbers3.append(numbers2[i])
        elif i % 2 == 0:
            numbers3.append(numbers2[i] * numbers2[i-1])
    if numbers3 != []:    
        print(sum(numbers3))
   
def smart_calc(user_input):
    if user_input == '/exit':
        print('Bye!')
        exit()
    elif user_input == '/help':
        print('The program calculates the sum of numbers')
    elif user_input.startswith('/'):
        print('Unknown command')
    elif user_input == '':
        None
    else:
        if len(uis) == 1 or (len(uis) > 1 and ('+' not in uis[1] and '-' not in uis[1])): #input variables
            var_input(user_input)
        else:
            calc(user_input)

        
var_dict = {'b': 8, 'c': 5, 'd': 121}
while True:
    user_input = 'variable = f'
    if '=' in ''.join(user_input):
        uis = ''.join(user_input.split()).replace('=', ' = ').split() #treat if there are no spaces in the variable determination
    else:
        uis = user_input.split()
    smart_calc(user_input)
    break

  

