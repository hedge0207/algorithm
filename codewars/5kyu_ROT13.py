def rot13(message):
    ans = ""
    for char in message:
        if not char.isalpha():
            ans += char
            continue
        base = ord("a") if char.islower() else ord("A")
        ans += chr(base + (ord(char) - base - 13) % 26)
    return ans