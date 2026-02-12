```python

T = int(input())
for test_num in range(1,1+T):
    N,w1,w2 = map(int,input().split())
    List = sorted(list(map(int,input().split())))
    answer = 0
    for i in range(1,1+ max(w1,w2)):
       answer += i*List.pop()
       if i < min(w1,w2)+1:
            answer += i*List.pop()
    print(f"#{test_num} {answer}")


```



```python

# 재귀 함수를 돌고 나오면 숫자를 뱉게 만들고 싶어요.
def find_matching_closing(s, start_index):
    if s[start_index] != '(':
        return -1 # 여는 괄호가 아닌 경우

    stack = []
    for i in range(start_index, len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if not stack:
                return i # 짝이 맞는 닫는 괄호 인덱스 반환
    return -1


def cal(S:str):
    #들어오면 () 여부 확인
    # 있으면 그거  풀어주고
    # 없으면 계산해서 출력
    tempS = S
    if '(' not in S:
        L =list(S.split("+"))
        NL =[]
        for i in L:
            if "*" in i:
                mul = 1
                A =list(map(int,i.split("*")))
                for a in A:
                    mul *= int(a)
                NL.append(mul)
            else:
                NL.append(int(i))
        return sum(NL)
    else:
        #스택으로 좌표 찾기...
        while '(' in tempS:
            start = tempS.find('(')
            end = find_matching_closing(tempS,tempS.find('('))
            tempS = tempS[:start]+ str(cal(tempS[start+1:end]))+tempS[end+1:]
        return cal(tempS)


for test_num in range(1,11):
    n = int(input())
    L = input()
    
    print(f'#{test_num} {cal(L)}')

```