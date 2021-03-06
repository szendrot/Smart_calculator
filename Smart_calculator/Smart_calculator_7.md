Description
In the final stage, it remains to add operations: multiplication *, integer division / and parentheses (...). They have a higher priority than addition + and subtraction -.

Here is an example of an expression that contains all possible operations:

3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)
The result is 121.

A general expression can contain many parentheses and operations with different priorities. It is difficult to calculate such expressions if you do not use special methods. Fortunately, there is a fairly effective and universal solution, using a stack, to calculate the most general expressions.

From infix to postfix

Earlier we processed expressions written in infix notation. This notation is not very convenient if an expression has operations with different priorities, especially when brackets are used. But we can use postfix notation, also known as Reverse Polish notation (RPN). In this notation, operators follow their operands. See several examples below.

Infix notation 1:

3 + 2 * 4
Postfix notation 1:

3 2 4 * +
Infix notation 2:

2 * (3 + 4) + 1
Postfix notation 2:

2 3 4 + * 1 +
To better understand the postfix notation, you can play with a converter.

As you can see, in postfix notation operations are arranged according to their priority and parentheses are not used at all. So, it is easier to calculate expressions written in postfix notation.

You can use a stack (LIFO) to convert an expression from infix to postfix notation. The stack is used to store operators for reordering. Here are some rules that describe how to create an algorithm that converts an expression from infix to postfix notation.

Add operands (numbers and variables) to the result (postfix notation) as they arrive.
If the stack is empty or contains a left parenthesis on top, push the incoming operator on the stack.
If the incoming operator has higher precedence than the top of the stack, push it on the stack.
If the precedence of the incoming operator is lower than or equal to that of the top of the stack, pop the stack and add operators to the result until you see an operator that has smaller precedence or a left parenthesis on the top of the stack; then add the incoming operator to the stack.
If the incoming element is a left parenthesis, push it on the stack.
If the incoming element is a right parenthesis, pop the stack and add operators to the result until you see a left parenthesis. Discard the pair of parentheses.
At the end of the expression, pop the stack and add all operators to the result.
No parentheses should remain on the stack. Otherwise, the expression has unbalanced brackets. It is a syntax error.

Calculating the result

When we have an expression in postfix notation, we can calculate it using another stack. To do that, scan the postfix expression from left to right:

If the incoming element is a number, push it into the stack (the whole number, not a single digit!).
If the incoming element is the name of a variable, push its value into the stack.
If the incoming element is an operator, then pop twice to get two numbers and perform the operation; push the result on the stack.
When the expression ends, the number on the top of the stack is a final result.
Here you can find an example and additional explanations on postfix expressions.

Objectives
Your program should support multiplication *, integer division / and parentheses (...). To do this, use infix to postfix conversion algorithm above and then calculate the result using stack.
Do not forget about variables; they, and the unary minus operator, should still work.
Modify the result of the /help command to explain all possible operators. You can write the output for the command in free form.
The program should not stop until the user enters the /exit command.
Note that a sequence of + (like +++ or +++++) is an admissible operator that should be interpreted as a single plus. A sequence of - (like -- or ---) is also an admissible operator and its meaning depends on the length. If a user enters a sequence of * or /, the program must print a message that the expression is invalid.
As a bonus, you may add the power operator ^ that has a higher priority than * and /.
> 2^2
4
> 2*2^3
16
Examples
The greater-than symbol followed by a space (>) represents the user input.

> 8 * 3 + 12 * (4 - 2)
48
> 2 - 2 + 3
3
> 4 * (2 + 3
Invalid expression
> -10
-10
> a=4
> b=5
> c=6
> a*2+b*3+c*(2+3)
53
> 1 +++ 2 * 3 -- 4
11
> 3 *** 5
Invalid expression
> 4+3)
Invalid expression
> /command
Unknown command
> /exit
Bye!