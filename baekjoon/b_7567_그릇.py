bowls = input()

height = 0
post_bowl = ""
for bowl in bowls:
    if bowl == post_bowl:
        height += 5
    else:
        height += 10
    post_bowl = bowl

print(height)