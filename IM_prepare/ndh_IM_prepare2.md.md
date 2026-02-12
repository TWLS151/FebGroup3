## IM prepare

### Portal 포탈
- 이 문제를 풀면서 어려웠던 점 : 처음에 왼쪽 포탈 범위 설정을 어떻게 하는지 정하는 것이 어려웠습니다.
```python
# Portal 포탈
# 요구사항 정리 -> 1번 방 제외 전부 포탈 2개(왼쪽, 오른쪽)이다. 처음 방문한 방 반드시 왼쪽 포탈 이용 후 재방문시 오른쪽
# 아이디어 -> P[1]과 P[N]은 의미가 없음에 주의하라 > P[1]은 출발지에서 재시작, P[N]은 동일한 방 호출이라서 의미 X ??
#          -> 리스트 인덱싱을 통해서 range를 반복문을 통해서 구하고 길이를 측정한다.

T = int(input())

for test in range(1, T+1):
    N = int(input())
    left_portal = list(map(int, input().split()))
    portal_pass_cnt = -1        # 첫 호출은 이동이 아니기 때문
    for n in range(1, N+1):     # 방의 수 만큼 순회
        portal_pass_cnt += 1    # 바깥 순회 카운트 증가
        if 1 < n < N:
            for i in range(left_portal[n-1]-1, n):  # 시작값과 끝값 변동
                portal_pass_cnt += 1    # 왼쪽 포탈 카운트 증가
    print(f'#{test} {portal_pass_cnt}')
```

### 스위치 켜고 끄기 백준 1244
- 이 문제를 풀면서 개선할 점 : range 함수의 활용에 대해서 미흡한 부분이 많다는 것을 느꼈습니다. 반복적으로 사용하는 식들에 대해서 변수 처리를 할 필요가 있습니다. 
```python
# 스위치 켜고 끄기 백준 1244
# 요구사항 정리 -> 남학생은 자기 번호의 배수 스위치 상태 변화, 여학생은 번호 좌우 대칭 최대 구간에 대해서 상태 변화
N = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())
for _ in range(student_num):
    S, L = map(int, input().split())
    if S == 1:                                  # 남학생의 경우
        multiple_range = N//L
        for i in range(1, multiple_range+1):
            switch_status[L*i-1] = 1 - switch_status[L*i-1]     # 스위치 상태 변화
    elif S == 2:                                # 여학생의 경우
        switch_status[L - 1] = 1 - switch_status[L - 1]
        for j in range(1, min(L-1, N-1 - (L-1)) + 1):
            if switch_status[L-1 - j] == switch_status[L-1 + j]:
                switch_status[L - 1 - j] = 1 - switch_status[L - 1 - j]
                switch_status[L - 1 + j] = 1 - switch_status[L - 1 + j]
            else:
                break           # 대칭 조건에 해당하지 않으면 즉시 중단
for p in range(0, N, 20):
    print(*switch_status[p : p + 20])
```

### 6190 SWEA 정곤이의 단조 증가하는 수
- 이 문제를 풀면서 개선할 점 : 첫 풀이에서 3중 for문을 사용하면서 시간 복잡도가 높아져서 문제 요구시간인 4초 이내에 계산을 완료하지 못했습니다. 
```python
# 6190 SWEA 정곤이의 단조 증가하는 수
# 요구사항 정리 -> N개의 정수들의 곱으로 생긴 단조 증가(1234, 오름차순) 숫자 중 최대값 찾기
# 리스트 순회에서 28과 70이 나오지 않는 문제가 발생 -> 제거와 함께 인덱스 번호가 변화하기 때문에 생기는 현상, 앞으로 주의하기
T = int(input())

def is_monotone_increasing(x):
    s = str(x)
    for k in range(len(s)-1):   # int 값을 str로 변환하여 인덱싱으로 단조 증가 판단
        if s[k] > s[k+1]:
            return False
    return True

for test in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    multiple_list = []
    for i in range(N-1):
        for j in range(i+1, N):
            multiple_list.append(num_list[i] * num_list[j])
    asc_list = [x for x in multiple_list if x > 10 and is_monotone_increasing(x)]
    if asc_list:
        print(f'#{test} {max(asc_list)}')
    else:
        print(f'#{test} -1')
```

### 배수 스위치 백준 12927
- 이 문제를 풀면서 어려웠던 점 : 탐욕 알고리즘을 응용하는 과정에 대해서 더 많은 학습이 필요하다는 것을 느꼈습니다. 
```python
# 배수 스위치 백준 12927
# 요구사항 정리 -> 전체 소등 스위치, 개별 스위치, 배수 번호 일괄 스위치 3가지 종류로 최소한의 시도로 전부 켜고 소등
electric = list(input())
N = len(electric)
count = 0

def multiple_switch_function(num):
    for j in range(1, N + 1):
        if j % num == 0:
            if electric[j - 1] == 'Y':
                electric[j - 1] = 'N'
            else:
                electric[j - 1] = 'Y'

def bulbs_off_check():
    for bulb in electric:
        if bulb == 'Y':
            return False  # 하나라도 켜져 있으면 실패
    return True  # 전부 꺼져 있으면 성공

for i in range(1, N + 1):
    # 현재 전구가 켜져 있는지 하나씩 확인 (개별 상태 확인)
    if electric[i - 1] == 'Y':
        # 켜져 있다면, 해당 번호의 '배수 스위치 기능'을 실행
        multiple_switch_function(i)
        count += 1

        if bulbs_off_check() == True:
            break  # 다 꺼졌으면 더 이상 스위치를 누를 필요가 없으니 탈출

print(count)
```