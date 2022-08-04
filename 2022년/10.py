def solution(lottos, win_nums):
    answer = []
    
    lottos.sort()
    win_nums.sort()
    
    result = 0
    cnt = 0
    for l in lottos:

        if l in win_nums:
            result+=1
    
        if l == 0:
            cnt+=1
          
    if result+cnt <= 1:
        answer.append(6)
    else:
        answer.append(7-(cnt+result))
    if result <= 1:
        answer.append(6)
    else:
        answer.append(7-result)
    return answer