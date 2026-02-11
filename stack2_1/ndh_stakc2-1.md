## stack2-1

### carrot packaging 당근 포장하기 SWEA 16811
- 이 문제를 풀면서 어려웠던 점 : 당근을 세 바구니에 담는 과정에서 동일한 크기의 당근들을 한 바구니에만 담아야 하는 제한사항을 구현하는 것이 어려웠습니다.
- 이 문제를 풀면서 개선할 점 : 초기값 설정에서 충분히 큰 값을 설정할 필요가 있다는 피드백을 받았습니다. 충분히 큰 값을 초기값으로 설정해야 하는 경우 `float('int')`를 사용하는 것이 좋다는 것을 배웠습니다.
```python
# carrot packaging 당근 포장하기 SWEA 16811
# 요구사항 정리 -> 5가지 조건에 맞도록 수확한 당근을 포장하는 작업이다.
# 아이디어 -> 수확한 N개의 당근에 대하여 N//3 개 만큼 포장하는 것이 박스당 최소 투입 용량이다.
#          -> N//2 의 값보다 같은 크기의 당근 수가 많으면 바로 탈출하고 -1 출력한다.
#          -> '당근 크기별 수량 = 해당 인덱스 번호' 형식으로 처리하면서 편리하게 수를 세는 방식으로 코드 구현, 최대 크기 30
T = int(input())

for test in range(1, T+1):
    carrot = int(input())
    harvest = list(map(int, input().split()))
    carrot_size_count = [0] * 31 # '당근의 크기별 수량 = 인덱스' ex) 크기가 9인 당근 개수 = 인덱스 9에 저장
    for h in harvest:
        carrot_size_count[h] += 1   # 당근의 크기에 따른 개수 인덱스 번호로 저장, 동일한 크기는 동일한 박스에 담기 위함
    carrot_size_kind = [k for k in carrot_size_count if k > 0]
    if len(carrot_size_kind) < 3 or max(carrot_size_count) > carrot//2: # 크기 종류가 3가지 미만, 또는 개수 초과
        print(f'#{test} -1')
        continue                            # 조건을 만족하지 못하면 다음 수확으로 넘어갑니다.
    check_num = 1000                        # 변화 확인을 위한 초기값 세팅
    for c1 in range(1, 29):                 # 인덱스 경계값 설정
        for c2 in range(c1 + 1, 30):        # 시작 범위 설정
            small_box_sum = sum(carrot_size_count[1:c1 + 1])            # 세 개의 박스에 각각의 크기 당근 배정
            middle_box_sum = sum(carrot_size_count[c1 + 1:c2 + 1])      # 각 박스에 몇 개의 당근이 들었는지 합산
            large_box_sum = sum(carrot_size_count[c2 + 1:])
            if small_box_sum >0 and middle_box_sum >0 and large_box_sum >0: # 조건 만족하는지 검사(빈 박스)
                if small_box_sum <= carrot//2 and middle_box_sum <= carrot//2 and large_box_sum <= carrot//2: # 최대값 초과 검사
                    sub = max(small_box_sum, middle_box_sum, large_box_sum) - min(small_box_sum, middle_box_sum, large_box_sum)
                    if sub < check_num:     # 계산 완료 후 초기값 갱신 진행
                        check_num = sub
    if check_num == 1000:                   # 초기값 갱신이 되지 않은 경우 실패
        print(f'#{test} -1')
    else:
        print(f'#{test} {check_num}')
```

### building Tower 탑 쌓기
- 처음 생각한 논리를 그대로 코드로 구현해서 문제를 해결할 수 있었습니다. 
```python
# building Tower 탑 쌓기
# 요구사항 정리 -> 전체 화물에서 각 탑의 높이만큼 중복 없이 개수 선택한다. (각 층 높이*화물)의 값이 최소가 되도록 작업
# 아이디어 -> 가장 높은 층에 가장 작은 화물 우선 배정한다. 작은 수를 높은 층부터 차례대로 채우는 코드 작성
#           -> 가장 작은 화물을 두 탑 중 가장 높은 층에 우선 배정한다.
#           -> 이후 두 탑의 높이가 같아지는 시점에서는 번갈아서 화물 배정한다.
T = int(input())

for test in range(1, T+1):
    N, W1, W2 = map(int, input().split())
    freight = sorted(list(map(int, input().split())), reverse=True) # 가장 작은 값부터 입력받기 위해서 역방향 정렬
    w1_freight = []         # w1 화물을 담을 리스트 생성
    w2_freight = []         # w2 화물을 담을 리스트 생성
    for n in range(W1+W2):
        item = freight.pop()        # pop 한 요소를 담을 변수 설정, 중복 코드 제거
        if W1 >= W2:                        # 탑 1의 높이가 탑 2 이상인 경우
            w1_freight.append(item*W1)      # pop 한 요소 추가하면서 층 높이 곱 연산 진행 1
            W1 -= 1                         # 층 높이 낮춤 1
        elif W1 < W2:                       # 탑 2가 더 높은 경우
            w2_freight.append(item*W2)      # pop 한 요소 추가하면서 층 높이 곱 연산 진행 2
            W2 -= 1                         # 층 높이 낮춤 2
    total_height = sum(w1_freight + w2_freight)
    print(f'#{test} {total_height}')
```

### 5431 SWEA 민석이의 과제 체크하기
- remove() 사용법 이외에는 풀이 과정 전부 매끄러웠습니다.
```python
# 5431 SWEA 민석이의 과제 체크하기
# 요구사항 정리 -> 수강생 N명 중 과제 제출 한 K명 제외한 사람들 오름차순으로 출력하는 문제
# 아이디어 -> N명의 번호로 리스트 생성하고 제출한 사람들 리스트에서 삭제 후 출력

T = int(input())

for test in range(1, T+1):
    N, K = map(int, input().split())
    submit_student = list(map(int, input().split()))
    all_student = [a for a in range(1, N + 1)]
    for s in submit_student:
        all_student.remove(s)
    print(f'#{test}', end=' ')
    print(*all_student)
```

### 4874 SWEA Forth
- 이 문제를 풀면서 어려웠던 점 : 다양한 예외처리 과정 중 피연산자의 과다 경우가 끝까지 생각하기 어려웠습니다. 이러한 예외처리의 관점에 대해서 더 공부하겠습니다.
```python
# 4874 SWEA Forth
# 요구사항 정리-> 후위연산postfix) 사칙연산 계산기를 코드로 구현한다.

T = int(input())

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token == '.':                    # 마무리 단계인지 확인
            if len(stack) == 1:             # 피연산자 과다한 경우 걸러내는 작업 수행, 정상 케이스만 통과
                return stack.pop()
            else:
                return "error"
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2 or token not in '+-*/':  # 피연산자 부족하게 입력되거나 정해지지 않은 값 입력의 경우
                return "error"
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0: return "error"   # 0으로 나누려는 경우 / 조기 반환 한줄로 처리 가능
                stack.append(int(left / right))
    return stack[0]

for test in range(1, T+1):
    postfix = input().split()   # split() 자체가 리스트를 반환하기 때문에 str 타입을 활용한다면 감쌀 필요 X
    print(f'#{test} {evaluate_postfix(postfix)}')
```

### 1224 계산기 3
- 1222, 1223, 1224 셋 다 사실상 동일한 문제였습니다.
```python
# 1224 계산기 3
# 요구사항 정리 -> 중위 표기법을 후위 표기법으로 변환하고 계산 완료하기
def infix_to_postfix(infix):    # 중위 연산자를 후위 연산자로 변환하는 함수
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,
    }
    stack = []
    result = []
    for token in infix:
        if token.isalnum():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)
    while stack:
        result.append(stack.pop())
    return ''.join(result)

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token == '.':                    # 마무리 단계인지 확인
            if len(stack) == 1:             # 피연산자 과다한 경우 걸러내는 작업 수행, 정상 케이스만 통과
                return stack.pop()
            else:
                return "error"
        if token.isdigit():
            stack.append(int(token))
        else:
            if len(stack) < 2 or token not in '+-*/':  # 피연산자 부족하게 입력되거나 정해지지 않은 값 입력의 경우
                return "error"
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0: return "error"   # 0으로 나누려는 경우 / 조기 반환 한줄로 처리 가능
                stack.append(int(left / right))
    return stack[0]

for test in range(1, 11):
    N = int(input())
    infix = input()
    print(f'#{test} {evaluate_postfix(infix_to_postfix(infix))}')
```