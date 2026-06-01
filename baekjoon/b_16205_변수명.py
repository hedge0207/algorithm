def change_to_snake_case(original_case: str, name: str):
    changed = ""
    if original_case == "1":
        for char in name:
            if char.isupper():
                changed += "_"
                changed += char.lower()
            else:
                changed += char
    else:
        for char in name:
            if not changed:
                changed += char.lower()
                continue
            if char.isupper():
                changed += "_"
                changed += char.lower()
            else:
                changed += char
    return changed

def change_to_camel_case(original_case: str, name: str):
    if original_case == "2":
        split = name.split("_")
        changed = split[0]
        for i in range(1, len(split)):
            changed += split[i][0].upper() + split[i][1:]
    else:
        changed = name[0].lower() + name[1:]
    return changed

def change_to_pascal_case(original_case: str, name: str):
    if original_case == "1":
        changed = name[0].upper() + name[1:]
    else:
        changed = ""
        split = name.split("_")
        for i in range(len(split)):
            changed += split[i][0].upper() + split[i][1:]
    return changed


case, var_name = input().split()
if case == "1":
    print(var_name)
    print(change_to_snake_case(case, var_name))
    print(change_to_pascal_case(case, var_name))
elif case == "2":
    print(change_to_camel_case(case, var_name))
    print(var_name)
    print(change_to_pascal_case(case, var_name))
else:
    print(change_to_camel_case(case, var_name))
    print(change_to_snake_case(case, var_name))
    print(var_name)