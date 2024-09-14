import re

user_input = input("> ")

operators = '[+-/*())(]'
user_numbers = re.split(operators, user_input)
user_operators = re.split('[\d]+', user_input)

if not re.search('[()]',user_input):
    print("nah bro there isnt a parenthesis'")

    #(1+1)*2

    #takes away weird blank spaces in the operator list
    for blank_values in user_operators:
        if blank_values == '':
            user_operators.remove(blank_values)
        else:
            pass

    for blank_values in user_numbers:
        if blank_values == '':
            user_numbers.remove(blank_values)
        else:
            pass



    print(user_numbers, user_operators)

    def math_operation(int_input_1,int_input_2,operation_symbol):
        int_answer = int()
        if operation_symbol == "*":
            int_answer =  int(int_input_1) * int(int_input_2) 

        elif operation_symbol == "/":
            int_answer = int(int_input_1) / int(int_input_2)

        elif operation_symbol == "+":
            int_answer = int(int_input_1) + int(int_input_2)

        elif operation_symbol == "-":
            int_answer = int(int_input_1) - int(int_input_2)

        return int_answer

    def list_to_operation(given_operators,given_numbers,operator: str):
        while operator in given_operators:

            operator_index = given_operators.index(operator)

            num_1_index = operator_index
            num_2_index = operator_index + 1

            num_1 = given_numbers[num_1_index]
            num_2 = given_numbers[num_2_index]

            given_numbers[num_1_index] = math_operation(num_1,num_2,operator)
            del given_numbers[num_2_index]
            del given_operators[operator_index]

            print(given_numbers,given_operators)

    while len(user_numbers) > 1:

        list_to_operation(user_operators,user_numbers,'*')

        list_to_operation(user_operators,user_numbers,'/')

        list_to_operation(user_operators,user_numbers,'+')

        list_to_operation(user_operators,user_numbers,'-')

        break



    print(user_numbers,user_operators)


    print(len(user_numbers))


else:
    print("yeah bro theres parenthesis'")
    user_formula_parenthesis = re.split('[()]',user_input)

    for blank_values in user_formula_parenthesis:
        if blank_values == '':
            user_formula_parenthesis.remove(blank_values)
        else:
            pass

    print(user_formula_parenthesis)
    pass


#"10+1*2"

#[1,0,"+",1,"*",2]

'''
    while '*' in user_operators:

        operator_index = user_operators.index('*')

        num_1_multiply_index = operator_index
        num_2_multiply_index = operator_index + 1

        num_1_multiply = user_numbers[num_1_multiply_index]
        num_2_multiply = user_numbers[num_2_multiply_index]

        user_numbers[num_1_multiply_index] = math_operation(num_1_multiply,num_2_multiply,'*')
        del user_numbers[num_2_multiply_index]
        del user_operators[operator_index]

        print(user_numbers,user_operators)


    while '/' in user_operators:

        division_index = user_operators.index('/')

        num_1_divide_index = division_index
        num_2_divide_index = division_index + 1

        num_1_divide = user_numbers[num_1_multiply_index]
        num_2_divide = user_numbers[num_2_multiply_index]

        user_numbers[num_1_multiply_index] = math_operation(num_1_divide,num_2_divide,'/')
        del user_numbers[num_2_multiply_index]
        del user_operators[operator_index]

        print(user_numbers,user_operators)


    while '+' in user_operators:

        division_index = user_operators.index('+')

        num_1_multiply_index = operator_index
        num_2_multiply_index = operator_index + 1

        num_1_multiply = user_numbers[num_1_multiply_index]
        _multiply = user_numbers[num_2_multiply_index]

        user_numbers[num_1_multiply_index] = math_operation(num_1_multiply,_multiply,'+')
        del user_numbers[num_2_multiply_index]
        del user_operators[operator_index]

        print(user_numbers,user_operators)


    while '-' in user_operators:

        division_index = user_operators.index('-')

        num_1_multiply_index = operator_index
        num_2_multiply_index = operator_index + 1

        num_1_multiply = user_numbers[num_1_multiply_index]
        _multiply = user_numbers[num_2_multiply_index]

        user_numbers[num_1_multiply_index] = math_operation(num_1_multiply,_multiply,'-')
        del user_numbers[num_2_multiply_index]
        del user_operators[operator_index]

        print(user_numbers,user_operators)
'''
        








'''
def tokenize(operation):
    token_pattern = r'\d+|[+-/*]'
    user_operation = re.findall(token_pattern,operation)

    return user_operation

print(tokenize(user_input))
'''