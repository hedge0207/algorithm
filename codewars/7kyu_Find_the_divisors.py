def divisors(integer):
    answers = []
    for i in range(2, integer):
        if not integer % i:
            answers.append(i)
    if not answers:
        answers = "{} is prime".format(integer)

    return answers
