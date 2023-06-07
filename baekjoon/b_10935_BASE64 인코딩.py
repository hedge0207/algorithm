def convert_to_binary(ascii_code):
    binary_string = ""
    while ascii_code:
        if ascii_code % 2 == 0:
            binary_string += "0"
        else:
            binary_string += "1"
        ascii_code //= 2

    while len(binary_string) != 8:
        binary_string += "0"

    return binary_string[::-1]


def get_base64_index(six_bits):
    index = 0
    position = 5
    for bit in six_bits:
        if int(bit):
            index += 2 ** position
        position -= 1

    return index


def make_base64_index():
    base64_index = {
        62: "+",
        63: "/"
    }
    num_to_plus = 65
    for i in range(62):
        if i == 26:
            num_to_plus += 6
        if i == 52:
            num_to_plus = -4
        base64_index[i] = chr(i + num_to_plus)

    return base64_index



base64_index = make_base64_index()

ascii_codes = [ord(char) for char in input()]
binary_string = ""
for ascii_code in ascii_codes:
    binary_string += convert_to_binary(ascii_code)

base64_encoded = ""
num_padding = 0
for i in range(0, len(binary_string), 6):
    six_bits = binary_string[i:i + 6]

    length = len(six_bits)
    if length != 6:
        num_padding = length % 3
        for _ in range(6 - length):
            six_bits += "0"

    print(base64_index[get_base64_index(six_bits)], end="")

for _ in range(num_padding):
    print("=", end="")

