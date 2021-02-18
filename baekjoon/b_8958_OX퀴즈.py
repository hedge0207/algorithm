for tc in range(int(input())):
    ox = input()

    score = 0
    total_score=0
    for i in ox:
        if i=="O":
            score+=1
            total_score+=score
        else:
            score=0
    print(total_score)


