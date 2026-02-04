# 1209 SWEA Sum
# 100x100 행렬 처리

for test in range(10):
    # 1. 테스트 케이스 번호 읽기
    line = input().strip()
    while not line:
        line = input().strip()
    T = int(line)

    # 2. 10,000개의 숫자를 한 리스트에 모으기
    matrix_numbers_1d = []
    while len(matrix_numbers_1d) < 10000:
        row_input = input().split()
        if row_input:
            matrix_numbers_1d.extend(map(int, row_input))

    # 3. 2차원 리스트로 변환
    matrix_numbers_2d = [matrix_numbers_1d[cnt*100 : (cnt+1)*100] for cnt in range(100)]
    
    sum_list = []

    # 대각선 합
    diagonal_number = 0
    for row in range(100):
        diagonal_number += matrix_numbers_2d[row][row]
    sum_list.append(diagonal_number)

    # 역대각선 합
    diagonal_re_number = 0
    for i in range(100):
        # row: i, col: 99-i (합이 항상 99)
        diagonal_re_number += matrix_numbers_2d[i][99-i]
    sum_list.append(diagonal_re_number)      

    # 행의 합
    for row in matrix_numbers_2d:
        sum_list.append(sum(row))

    # 열의 합
    for col in range(100):
        col_sum_number = 0
        for row in range(100):
            col_sum_number += matrix_numbers_2d[row][col]
        sum_list.append(col_sum_number)

    # 결과 출력
    output = max(sum_list)
    print(f'#{T} {output}')