# 4861 SWEA 회문
# 요구사항 정리 -> N*N 글자판에서 길이가 M인 회문을 찾아 출력
# 아이디어 -> N줄의 행에 대해선 입력과 동시에 정리된다. 열에 대해서 처리하고 회문 찾는 작업 수행 코드 작성

T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    str_list = [str(input().strip()) for row in range(N)]

    # 열에 대해서 정보 받아오기
    for col in range(N):
        str_col = ""
        for row in range(N):
            str_col += str_list[row][col]
        str_list.append(str_col)

    # str_list 내의 회문 탐색
    # 문자 끝부분 공백을 없애는 로직도 추가
    # N과 M의 값이 다른 경우 순회하는 코드 추가
    for char in str_list:
        if N == M:
            if char == char[::-1]:
                print(f'#{test + 1} {char}')
        else:
            for search in range(N - M + 1):
                mini_char = char[search : search+M]
                if mini_char == mini_char[::-1]:
                    print(f'#{test+1} {mini_char}')