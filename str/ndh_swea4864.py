# 4864 SWEA 문자열 비교
# 요구사항 정리 -> 입력받은 두 문자열 중 str1이 str2 내에 동일하게 존재하면 1 아니면 0 출력
# 아이디어 -> str1의 길이 측정하고 길이만큼 str2 글자 인덱스 번호마다 시작점 지정해서 순회 생성, 새로운 리스트 담기

T = int(input())

for test in range(T):
    str1 = str(input().strip())
    str2 = str(input().strip())
    str_list = []
    num = 0

    # str1의 길이만큼 str2의 모든 인덱스(마지막 str1 길이만큼의 인덱스 제외)
    # 시작점으로 만든 단어들 생성, str_list에 추가
    for s in range(len(str2)-len(str1)+1):
        slice_char = str2[s:len(str1)+s]
        str_list.append(slice_char)

    # str_list 순회하면서 str1과 str2 내의 단어들 비교
    for char in str_list:
        if str1 == char:
            num = 1
    print(f'#{test+1} {num}')