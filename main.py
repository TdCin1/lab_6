# 8 digit passcode

def encode_password(password):
    new_password = ""
    for i in password:
        temp = str(int(i)+3)
        if int(temp) >= 10:
            temp = int(temp) - 10
        new_password += str(temp)
    return new_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode_password(password)

        if choice == 2:
            pass

        if choice == 3:
            exit()


