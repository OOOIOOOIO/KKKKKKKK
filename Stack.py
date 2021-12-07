# stack이 비어있는지 확인하는 함수 : pop, peek에 쓰임
def isStackEmpty() :
    global SIZE, stack, top
    if top == -1 :
        return True
    return False


# stack이 가득 찼는지 확인하느 함수 : push에 쓰임
def isStackFull() :
    global SIZE, stack, top
    if top >= SIZE :
        return True
    return False


# stack에 추가하는 함수
def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print("스택이 꽉 찼습니다")
        return

    top += 1
    stack[top] = data


# stack에서 추출하는 함수
def pop() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        print("추출할 데이터가 없습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


# stack의 맨 위 데이터를 확인하는 함수
def peek() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        print("확인할 데이터가 없습니다")
        return None

    return stack[top]


# 전역변수
SIZE = int(input("스택의 크기를 입력해주세요 -->"))
stack = [None for _ in range(SIZE)]
top = -1


# 메인 함수
if __name__ == '__main__' :

    for i in range(SIZE) :
        push(input())

    print("pop : ", pop())

    print("peek : ", peek())

    print("stack : ", stack)
