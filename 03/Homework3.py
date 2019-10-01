def p01():  # Homwwork 01
    print("Hello, world!")


def p02_1():  # Homework 02-01
    user_name = input('What is your user name? ')
    print('Hello, {}'.format(user_name))


def p02_2():  # Homework 02-02
    temperature_C = input("Please key in temperature in Celsius: ")  # read input
    temperature_F = float(temperature_C) * 1.8 + 32  # convert the inout into floating point number
    print("Temperature in Fahrenheit: {:.2f}".format(temperature_F))  # keep 2 decimals in result


def p03(program):  # Execute the selected program
    if program == 'p01':
        p01()
    elif program == 'p02-1':
        p02_1()
    elif program == 'p02-2':
        p02_2()
    else:
        print('Invalid program!')
    print('---------------------------------------------------------------------')


if __name__ == '__main__':
    while True:
        print('p01: Hello World')
        print('p02-1: Hello User')
        print('p02-2: Convert Celsius to Fahrenheit')
        print('exit: Terminate the program')
        print('---------------------------------------------------------------------')
        program = input('Please key in the program that you want to execute: ')
        print('---------------------------------------------------------------------')
        if program == 'exit':
            print('Thanks for your usage!')
            break
        else:
            p03(program)
