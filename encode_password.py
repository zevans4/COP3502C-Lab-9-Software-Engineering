def encode_password(password):
    password_list = [int(i) for i in str(password)]
    encoded_password_list = [str(num+3) for num in password_list]
    encoded_password = ''.join(encoded_password_list)
    return encoded_password
