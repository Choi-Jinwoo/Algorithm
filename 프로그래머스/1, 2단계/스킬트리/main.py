def can_use(master, skill_order, use_skill):
    list_skill_order = list(skill_order)
    use_skill_idx = list_skill_order.index(use_skill)
    must_master_skills = list_skill_order[:use_skill_idx]

    for skill in must_master_skills:
        if skill not in master:
            return False

    return True


def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        master_skill = []
        list_skill_tree = list(skill_tree)

        is_poss = True
        for skill_tree_item in list_skill_tree:
            # 스킬 안에 있다면
            if skill_tree_item in skill:
                if not can_use(master_skill, skill, skill_tree_item):
                    is_poss = False
                else:
                    master_skill.append(skill_tree_item)

        if is_poss:
            cnt += 1

    return cnt



print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
