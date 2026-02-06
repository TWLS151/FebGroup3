# 5356 SWEA 의석이의 세로로 말해요
# 요구사항 정리 -> 5줄의 문자열 입력받음 입력받은 문자열 공백은 무시하고 세로로 바라본 내용 출력
# 아이디어 -> 문자열 인덱싱 진행

T = int(input())

for test in range(T):
    wall_char = [input().strip() for _ in range(5)]
    output = " "
    for col in range(5):
        for row in range(5):
            if col < len(wall_char[row]):
                output += wall_char[row][col]
    print(f'#{test+1} {output}')