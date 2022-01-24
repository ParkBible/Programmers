def solution(id_list, report, k):
    
    # 중복 제거
    report_new = []
    for i in report:
        if i not in report_new:
            report_new.append(i)

    # 신고당한 횟수
    b = [0 for i in range(len(id_list))]
    tar_id = []
    target = []
    req = []
    answer = [0 for i in range(len(id_list))]
    
    # 신고당한 사람의 아이디를 tar_id에 기록.
    for i in range(len(report_new)):
        tar_id.append(report_new[i].split(" ")[1])
    
    # id_list 인덱스별로 신고당한 횟수 기록
    for i in range(len(id_list)):
        for j in range(len(tar_id)):
            if(id_list[i] == tar_id[j]):
                b[i] = b[i] + 1

    # b에서 신고당한 횟수가 k회 넘는다면 그 인덱스를 뽑아서 id_list에서 이름 뽑아 target에 기록
    for i in range(len(b)):
        if(b[i] >= k):
            #print(id_list[i])
            target.append(id_list[i])
    
    # target에 들어있는 요소와 report에 들어있는 요소를 하나하나 비교하여, 맞으면 신고자 이름을 뽑아서 req에 넣음
    if(len(target) != 0):
        for i in range(len(report_new)):
            for j in range(len(target)):
                if(report_new[i].split(" ")[1] == target[j]):
                    req.append(report_new[i].split(" ")[0])
    print(req)
    # id_list에 해당하는 req에 +1을 해줌.
    for i in range(len(id_list)):
        for j in range(len(req)):
            if(id_list[i] == req[j]):
                answer[i] = answer[i] + 1
    return answer


# 딕셔너리를 사용했으면 쉽게 풀릴수도 있는 문제였다...

# 내 코드가 오래걸린 이유 : target을 report와 하나하나 비교해야 해서, target개수 * report개수 만큼 비교작업을 해야함. 즉 report가 늘어날수록 시간이 오래걸림.

# 반면 모범답안의 코드는 id_list의 요소들과 r.split()[0]을 4번씩만 비교하면 됨.(.index 로)

# 인덱스 추출 : mylist.index(”요소”)

# 딕셔너리 접근 : mydict[”키값”] 하면 value값 추출 가능.