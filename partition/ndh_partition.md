## Partition

### 4880 SWEA 토너먼트 카드게임
- 이 문제를 풀면서 어려웠던 점 : merge 단계에서 두 값을 합치는 게 아니라 두 승자 인덱스를 비교해 최종 승자를 반환해야 한다는 점이 일반적인 병합 정렬과 달라 혼란스러웠습니다.
- 이 문제를 풀면서 개선할 점 : 가위바위보 승패 로직을 `if-elif` 나열 대신 `(left - right) % 3` 같은 수식으로 단순화할 수 있다.
```python
# 4880 SWEA 토너먼트 카드게임

def merge(left_idx, right_idx):

    left_card = cards[left_idx]
    right_card = cards[right_idx]

    # 같은 카드면 인덱스 번호가 작은 사람이 승리하도록 처리
    if left_card == right_card:
        if left_idx < right_idx:
            return left_idx
        else:
            return right_idx

    # 가위(1) 바위(2) 보(3)
    # 가위 > 보
    if left_card == 1 and right_card == 3:
        return left_idx
    if left_card == 3 and right_card == 1:
        return right_idx

    # 바위 > 가위
    if left_card == 2 and right_card == 1:
        return left_idx
    if left_card == 1 and right_card == 2:
        return right_idx

    # 보 > 바위
    if left_card == 3 and right_card == 2:
        return left_idx
    if left_card == 2 and right_card == 3:
        return right_idx


def merge_sort_rps(left, right):

    if left == right:   # 재귀함수 종료를 위한 조건 추가
        return left     # 1명만 참가한 경우 가지치기로 처리

    # 1단계: 분할
    mid = (left + right) // 2

    # 2단계: 정복
    left_winner = merge_sort_rps(left, mid)
    right_winner = merge_sort_rps(mid + 1, right)

    # 3단계: 병합 (두 승자 비교)
    final_winner = merge(left_winner, right_winner)

    return final_winner


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cards = [0] + arr
    winner_idx = merge_sort_rps(1, N)
    print(f"#{tc} {winner_idx}")
```

### 5202 SWEA 화물 도크
- 이 문제를 풀면서 어려웠던 점 : 그리디 선택 기준을 "시작 시간 기준 정렬"로 잘못 접근할 수 있었다.
- 이 문제를 풀면서 개선할 점 : `last_end_time = 0` 초기값 설정과 `start >= last_end_time` 조건이 핵심인데, 경계값(`>=` vs `>`)을 헷갈리지 않도록 예제로 직접 검증하는 습관을 들이면 좋다.
```python
# 5202 SWEA 화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_hours = [list(map(int, input().split())) for _ in range(N)]
    work_hours.sort(key=lambda x: x[1])

    count = 0
    last_end_time = 0  # 마지막 작업이 끝난 시간

    for start, end in work_hours:
        if start >= last_end_time:
            count += 1
            last_end_time = end  # 종료 시간 업데이트

    print(f"#{tc} {count}")
```

### 1240 SWEA 단순 2진 암호코드
- 이 문제를 풀면서 어려웠던 점 : 암호코드의 위치를 앞에서부터 찾는 게 아니라 뒤에서(`rfind`) 기준으로 잡아야 한다는 점이 처음엔 헷갈렸다.
- 이 문제를 풀면서 개선할 점 : `found = set()`으로 중복을 걸러내는 방식은 좋지만, 행마다 `set`을 초기화하지 않고 전체 루프 밖에 선언한 점은 다른 테스트케이스 간 의도치 않은 충돌을 유발할 수 있다. 
```python
# 1240 SWEA 단순 2진 암호코드
CODE = {
    '0001101': 0, '0011001': 1, '0010011': 2,
    '0111101': 3, '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7, '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    found = set()  # 중복 방지

    for _ in range(N):
        line = input().strip()

        # 1이 없는 행은 스킵
        if '1' not in line:
            continue

        # 끝에서 마지막 1의 위치 찾기
        end = line.rfind('1') + 1  # 끝 인덱스
        start = end - 56  # 8자리 × 7비트 = 56비트

        if start < 0:
            continue

        code_str = line[start:end]

        if code_str in found:
            continue
        found.add(code_str)

        # 7비트씩 8개 디코딩
        digits = []
        valid = True
        for i in range(8):
            chunk = code_str[i * 7:(i + 1) * 7]
            if chunk not in CODE:
                valid = False
                break
            digits.append(CODE[chunk])

        if not valid:
            continue

        # 유효성 검사: 홀수 위치 × 3 + 짝수 위치
        # 인덱스 0,2,4,6 (홀수 번째) × 3 + 인덱스 1,3,5,7 (짝수 번째)
        check = (digits[0] + digits[2] + digits[4] + digits[6]) * 3 \
                + (digits[1] + digits[3] + digits[5] + digits[7])

        if check % 10 == 0:
            print(f"#{tc} {sum(digits)}")
        else:
            print(f"#{tc} 0")
```