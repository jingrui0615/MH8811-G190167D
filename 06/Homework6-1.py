import password_generator

if __name__ == '__main__':
    length=input("Please enter the length of password:")
    password=password_generator.genPassword(int(length))
    print(password)