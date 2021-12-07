"""
                        < 11.03 퀴즈 >
                                                    스마트자동차학과
                                                    20181578
                                                    김성호

- Queue class 정의
- imEmpty() 구현
- enQueue() 구현
- deQueue() 구현
"""

# 노드 생성
class Node :
    def __init__(self, data) :
        self.data = data
        self.link = None


# 큐 클래스
class Queue() :
    def __init__(self) :
        self.front = None
        self.rear = None

    # 비어있는지 확인
    def isEmpty(self) :
        if self.front == None :
            return True
        return False


    # 삽입하기
    def enQueue(self, data) :
        new_node = Node(data)

        # 처음
        if(self.isEmpty()) :
            self.front = new_node
            self.rear = new_node

        # 두번째부터
        self.rear.link = new_node
        self.rear = self.rear.link


    # 추출하기
    def dequeue(self):
        if(self.isEmpty()) :
            print("큐가 비어있습니다.")

        dequeueData = self.front.data
        self.front = self.front.link


    # 출력하기
    def printData(self) :
        curPos = self.front
        while (curPos.link != None) :
            print(curPos.data, end = " ")

            curPos = curPos.link

        print(curPos.data)

        # if(curPos.link == None) :
        #     print(curPos.data)


if __name__ == '__main__' :
    queue = Queue()

    # 추가하기
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.enQueue(4)
    queue.enQueue(5)

    # print(queue.rear.data)

    # 출력하기
    queue.printData()

    # 추출하기
    queue.dequeue()
    queue.dequeue()

    # 추출한 후 출력하기
    queue.printData()
