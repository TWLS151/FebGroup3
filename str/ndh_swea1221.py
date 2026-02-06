# 1221 SWEA GNS
# 요구사항 정리 -> "ZRO" 등 영어 숫자들의 정렬 진행하는 코드 작성
# 기준이 되는 숫자 순서
order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for _ in range(T):
    case_num, case_len = input().split()
    eng_num_list = input().split()

    # 각 단어가 몇 번 나왔는지 저장할 공간(딕셔너리) 만들기
    counts = {word: 0 for word in order}

    # 입력받은 리스트를 돌며 개수 세기
    for eng in eng_num_list:
        counts[eng] += 1

    # 결과 출력하기
    print(case_num)
    for word in order:
        # 해당 단어를 개수만큼 반복해서 출력
        print((word + " ") * counts[word], end="")
    print() # 줄바꿈