def add(value1, value2):
    return value1 + value2


def subtract(value1, value2):
    return value1 - value2


def divide(value1, value2):
    try:
        return value1 / value2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


def multiply(value1, value2):
    return value1 * value2


def get_input_values():
    try:
        first_value = int(input('Enter the first value: '))
        second_value = int(input('Enter the second value: '))
        return first_value, second_value
    except ValueError as e:
        print('The given value cannot be calculated')
        quit()
        


def main():
    operations = {
        1: ('Addition', add),
        2: ('Subtraction', subtract),
        3: ('Division', divide),
        4: ('Multiplication', multiply),
        5: ('Exit', None)
    }

    while True:
        print('''
Select an operation:
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Exit
''')
        try:
            operation = int(input('Enter the operation number: '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')
            continue

        if operation in operations:
            if operation == 5:
                print('Exited')
                break

            operation_name, operation_function = operations[operation]
            first_value, second_value = get_input_values()
            result = operation_function(first_value, second_value)
            print(f'Result of {operation_name}: {result}')
        else:
            print('Please enter a valid operation number (1-5).')


if __name__ == '__main__':
    main()