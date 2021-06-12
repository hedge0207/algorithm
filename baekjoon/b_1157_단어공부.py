word = input().upper()
count_dict = {}

alphabet_list = list(word)

for alphabet in alphabet_list:
    ascii_code = ord(alphabet)
    if ascii_code in count_dict:
        count_dict[ascii_code] += 1
    else:
        count_dict[ascii_code] = 1

is_only = True
max_count = 0
result = 0

for k, v in count_dict.items():
    if max_count == v:
        is_only = False

    if max_count < v:
        max_count = v
        result = k
        is_only = True

if is_only:
    print(chr(result))
else:
    print("?")
