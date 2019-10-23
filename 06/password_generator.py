import random
import string


def genPassword(n):
    if n < 4:
        print("[Error]: Password length at least 4!")
        exit(1)

    digits = string.digits
    letters_upper = string.ascii_uppercase
    letters_lower = string.ascii_lowercase
    symbols = string.punctuation
    all_string = digits + letters_upper + letters_lower + symbols

    digit = random.sample(digits, 1)
    letter_upper = random.sample(letters_upper, 1)
    letter_lower = random.sample(letters_lower, 1)
    symbol = random.sample(symbols, 1)
    others=[]
    for i in range(n-4):
        others.append(random.choice(all_string))
    password = digit + letter_upper + letter_lower + symbol + others
    # print("before shuffle:", password)
    random.shuffle(password)
    # print("after shuffle:", password)
    password_str = "".join(password)

    return password_str


if __name__ == '__main__':
    length = 12
    password = genPassword(length)
    print(password)
