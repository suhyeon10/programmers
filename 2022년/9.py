from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for r in report:
        a,b = r.split()

        user[a].add(b)
        cnt[b] += 1

    print(user)

    for id in id_list:
        result = 0

        for u in user[id]:
            if cnt[u]>=k:
                result+=1
        
        answer.append(result)

    print(answer)
    
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)