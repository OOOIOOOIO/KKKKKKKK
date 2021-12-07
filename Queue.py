
def isQueueEmpty() :
    global SIZE, queue, front, rear

    if rear == front :
        return True
    return False


def isQueueFull() :
    global SIZE, queue, front, rear

    if rear == SIZE - 1 :
        return True
    return False


def enQueue(data) :
    global SIZE, queue, front, rear
    if(isQueueFull()) :
        print("큐가 꽉 차서 더이상 추가하지 못 합니다.")
        return

    rear += 1
    queue[rear] = data


def deQueue() :
    global SIZE, queue, front, rear
    if(isQueueEmpty()) :
        print("큐가 비어있어 더이상 추출하지 못 합니다.")
        return

    front += 1
    deQueueData = queue[front]
    queue[front] = None
    return deQueueData


def peek() :
    global SIZE, queue, front, rear

    if(isQueueEmpty()) :
        print("큐에 데이터가 존재하지 않습니다.")
        return

    return queue[front+1]


SIZE = int(input("큐 크기를 입력하세요 -->"))
queue = [None for _ in range(SIZE)]
front, rear = -1, -1



if __name__ == '__main__' :

    for i in range(SIZE) :
        enQueue(input())

    print("deQueue : ", deQueue())
    print("peek : ", peek())
    print(queue)
