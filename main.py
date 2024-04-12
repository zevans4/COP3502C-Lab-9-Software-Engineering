def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        def decode_password(encoded_password):
            def decoder(encoded_password):
                decoded = [(int(char) - 3) % 10 for char in encoded_password]
                return ''.join(map(str, decoded))

            pass

        if option == 3: # Quit
            return # BUHBYE!

        if option == 1: # Encode
            password = input("Please enter your password to encode: ")
            encoded_password = encoded_password(password)
            print("Your password has been encoded and stored!")

        if option == 2: # Decode
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

if __name__ == '__main__':
    main()
