# Shenyu Zhou

from version_control_2 import decode_password


def encode(init_code):
    new_code = []

    for i in init_code:
        new_code.append(int(i) + 3)

    encoded = "".join(map(str, new_code))

    print("Your password has been encoded and stored!" + "\n")

    return encoded

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:

            init_code = list(input("Please enter your password to encode: "))

            encoded = encode(init_code)

        elif option == 2:

            decode_password(init_code)

            pass

        elif option == 3:
            exit()


