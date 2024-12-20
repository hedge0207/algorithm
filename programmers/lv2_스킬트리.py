def solution(skill, skill_trees):
    answer = 0
    skill_set = set(list(skill))
    for skill_tree in skill_trees:
        prev_skill_idx = 0
        for skill_name in skill_tree:
            if skill_name not in skill_set:
                continue
            if skill_name != skill[prev_skill_idx]:
                break
            prev_skill_idx += 1
        else:
            answer += 1

    return answer