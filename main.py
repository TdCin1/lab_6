# 8 digit passcode

def encode_password(password):
    new_password = ""
    for i in password:
        temp = str(int(i)+3)
        if int(temp) >= 10:
            temp = int(temp) - 10
        new_password += str(temp)
    return new_password
