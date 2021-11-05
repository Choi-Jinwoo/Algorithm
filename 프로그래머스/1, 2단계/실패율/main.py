def solution(N, failed_stages):
    stages = []
    for i in range(N):
        stages.append({
            'count': 0,
            'fail_count': 0,
            'stage': i + 1,
            'percent': 0.0
        })

    all_clear = 0
    for failed_stage in failed_stages:
        if failed_stage == N + 1:
            all_clear += 1
        else:
            for i in range(failed_stage - 1):
                stages[i]['count'] += 1

            stages[failed_stage - 1]['fail_count'] += 1

    for stage in stages:
        if stage['count'] == 0 and all_clear == 0:
            stage['percent'] = 0
        else:
            stage['percent'] = stage['fail_count'] / (stage['count'] + all_clear)

    sorted_stages = sorted(stages, key=lambda x: (-x['percent'], x['stage']))
    print(sorted_stages)

    return [stage['stage'] for stage in sorted_stages]


print(solution(4, [4, 4, 4, 4, 4]))
