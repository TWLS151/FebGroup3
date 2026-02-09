# 오늘은 스택을 배웠어요!
스텍이 어렵다고 느끼고 점심으로 스테기 먹었어요!


## 4873 괄호검사  => 기본 개념을 이용해 풀었습니다.
```python
T  = int(input())
for test_num in range(1,T+1):
    L=[]
    L += input()
    stack = []
    for i in L:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_num} {len(stack)}')


```


## 1234 비밀번호
어떻게 비밀번호가 1234 이거 힙합이네요
```python

for test_num in range(1,10+1):
    A,B = input().split()
    L=[]

    L += B
    stack = []
    for i in L:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_num} ',*stack,sep='')
```


## 괄호 짝 짓기
```python

def check_brackets(string):
    stack = []

    for char in string:
        # -------------------------------------------------
        # [실습 1] 여는 괄호 처리
        # -------------------------------------------------
        # 문자열 '([{' 안에 char가 포함되어 있다면 여는 괄호입니다.
        if char in '([{<':
            # TODO: 여는 괄호는 나중에 짝을 맞추기 위해 스택에 넣습니다(push).
            stack.append(char)
            pass 
            
        # -------------------------------------------------
        # [실습 2] 닫는 괄호 처리
        # -------------------------------------------------
        # 문자열 ')]}' 안에 char가 포함되어 있다면 닫는 괄호입니다.
        elif char in ')]}>':
            
            # 1. 닫는 괄호가 나왔는데 스택이 비어있다면? (여는 괄호 부족)
            # TODO: 스택의 길이(len)를 확인하여 비어있으면 -1 반환
            if len(stack) ==0:
                return 0
            
            # 2. 스택에서 가장 최근에 넣은 여는 괄호를 꺼냅니다(pop).
            # TODO: pop 연산 수행
            open_char = stack.pop()
            
            # 3. 짝이 맞는지 일일이 확인합니다. (하나라도 안 맞으면 실패)
            # - 소괄호 짝 검사
            if char == ')' and open_char != '(':
                return 0
            
            # - 대괄호 짝 검사
            # TODO: 현재 문자가 ']' 인데 꺼낸 문자가 '[' 가 아니라면?
            elif char == ']' and open_char != '[':
            
                return 0
                
            # - 중괄호 짝 검사
            # TODO: 현재 문자가 '}' 인데 꺼낸 문자가 '{' 가 아니라면?
            elif char == '}' and open_char != '{':
                return 0
            elif char == '>' and open_char != '<':
                return 0
            
        # 괄호가 아닌 다른 문자(숫자 등)는 그냥 넘어갑니다.
        else:
            continue
            
    # -------------------------------------------------
    # [실습 3] 최종 결과 판별
    # -------------------------------------------------
    # 반복문이 다 끝났는데 스택에 뭔가 남아있다면? (여는 괄호 과다)
    # TODO: 스택이 비어있는지 확인하여 결과 반환
    if len(stack) == 0:
        return 1  # 성공 (깔끔하게 비어있음)
    else:
        return 0 # 실패 (잔여물 있음)



for tc in range(1, 10 + 1):
    T = int(input())
    line = input()
    print(f'#{tc} {check_brackets(line)}')

```

## 파스칼 삼각형...
```python
#하지만 풀었죠?
T = int(input())
pascal = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]]
for test_num in range(1,T+1):
    N = int(input())
    print(f'#{test_num}')
    for i in range(N):
        print(*pascal[i])

```