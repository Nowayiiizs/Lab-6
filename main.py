# Shenyu Zhou

print("Menu")
print("-" * 13)
print("1. Encode")
print("2. Decode")
print("3. Quit")

option = int(input("Please enter an option: "))

if option == 1:

    init_code = list(input("Please enter your password to encode: "))
    new_code = []

    for i in init_code:
        new_code.append(int(i) + 3)

    code_str = str(new_code)

    print("Your password has been encoded and stored!")

elif option == 2:
    pass

elif option == 3:
    exit()


