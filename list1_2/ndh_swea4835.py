# 4835 SWEA 구간합
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램의 작성 = 리스트 정렬하고 (끝값 M개 합) - (첫값 M개 합)
# 하지만 위의 요구사항대로 코드를 구현했는데 테스트케이스 답과 너무 다르다
# 내가 문제를 잘못 이해하고 있었다. 리스트를 정렬해서는 안된다. 이미지가 정렬된 숫자가 나와있어서 오해했다. 정렬되지 않은 수의 합이다.

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        sum_number = 0              # 값 초기화
        sum_number = sum(number_list[i:M+i])
        sum_list.append(sum_number)
    sum_list.sort()
    output_number = sum_list[-1] - sum_list[0]

    print(f'#{t+1}', end=' ')
    print(output_number)

    # 37643 - 