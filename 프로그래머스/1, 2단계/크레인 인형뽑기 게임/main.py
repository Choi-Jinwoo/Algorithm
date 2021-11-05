def solution(board, moves):
    done = []

    answer = 0
    for move in moves:
        for b in board:
            if b[move - 1] != 0:
                if len(done) > 0 and done[-1] == b[move - 1]:
                    answer += 2
                    done.pop()
                else:
                    done.append(b[move - 1])
                b[move - 1] = 0
                break

    return answer
