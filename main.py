# 8 digit passcode
def decode(password):
    oldPass = ""
    for i in range(0, len(password)):
        digit = (int(password[i:i+1]) - 3)
        if digit < 0:
            digit = digit + 10
        oldPass = oldPass + str(digit)
    return oldPass
def encode(password):
    new_password = ""
    for i in password:
        temp = str(int(i)+3)
        if int(temp) >= 10:
            temp = int(temp) - 10
        new_password += str(temp)
    return new_password

def main():
    encode_password = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode(password)

        if choice == "2":
            print("The encoded password is " + encoded_password + ", and the original password is " + decode(encoded_password) + ".")

        if choice == "3":
            exit()

if __name__ == '__main__':
    main()


