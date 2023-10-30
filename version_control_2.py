
def decode_password(encoded_data):
    decoded_data = ''
    for i in encoded_data:
        decoded_data += str(int(i) - 3)
    print(f'The encoded password is {encoded_data}, and the original password is {decoded_data}.')
