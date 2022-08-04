def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    print(new_id)
    
    # 2단계
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    
    # 3단계
    while '..'  in answer:
        answer = answer.replace('..', '.')


    # 4단계
    answer = answer[1:] if answer[0] =='.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1]=='.' else answer

    # 5단계
    answer = "a" if answer == "" else answer

    # 6단계
    if len(answer)>15:
        answer = answer[:15]
        if answer[-1]==".":
            answer = answer[:-1]

    # 7단계
    if len(answer)<3:
        answer += answer[-1] * (3-len(answer))    
    print(answer)

    return answer



solution("1")