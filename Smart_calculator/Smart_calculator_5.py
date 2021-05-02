# write your code here
import math
def calc(user_input):
    numbers1 = [i for i in user_input.split()]
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
        calc(user_input)

while True:
    user_input = '+17 ++ 9 -- 3 --- 25'
    smart_calc(user_input)
    break
