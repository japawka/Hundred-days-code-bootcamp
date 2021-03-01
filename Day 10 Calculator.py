from hangman_art import calc_logo

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    print(calc_logo)
    num1 = float(input("what is the first number "))
    should_continue = True
    while should_continue:
        for key in operations:
            print(key, end=" ")
        operator = input(f" - Pick an operator  ")
        num2 = float(input("what is the next number "))

        function = operations[operator]
        result = function(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        question = input(f"Type 'y' to calculate with {result} or type 'n' to start new calculation or 'e' to exit ")

        if question ==  'y':
            num1 = result
        elif question ==  'n':
            calculator()
        else:
            should_continue = False

calculator()