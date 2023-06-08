def make_base64_index():
    base64_index = {
        "+": 62,
        "/": 63
    }
    num_to_plus = 65
    for i in range(62):
        if i == 26:
            num_to_plus += 6
        if i == 52:
            num_to_plus = -4
        base64_index[chr(i + num_to_plus)] = i

    return base64_index


def convert_to_binary(num):
    binary_string = ""
    while num:
        if num % 2 == 0:
            binary_string += "0"
        else:
            binary_string += "1"
        num //= 2

    while len(binary_string) != 6:
        binary_string += "0"

    return binary_string[::-1]

def get_ascii_value(binary):
    num = 0
    position = 7
    for bit in binary:
        if int(bit):
            num += 2 ** position
        position -= 1
    if num:
        return chr(num)

base64_index = make_base64_index()
base64_encoded_text = input()

binary_string = ""
num_padding = 0
for char in base64_encoded_text:
    if char == "=":
        num_padding += 1
        continue
    binary_string += convert_to_binary(base64_index[char])

for i in range(0, len(binary_string), 8):
    char = get_ascii_value(binary_string[i:i+8])
    if char:
        print(char, end="")