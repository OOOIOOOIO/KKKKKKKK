"""
스마트자동차학과
20181578
김성호

1차 과제
삽입 : insertNode(data)
삭제 : deleteNode(data)
탐색 : findNode(data)
구현하기
"""

class Node() :
    def __init__(self) :
        self.data = None
        self.frontLink = None # 앞(일반적인 링크드리스트의 링크)
        self.backLink = None # 뒤


def insertNode(findData, data) :
    global head, memory, curPosition, prevNode

    # 첫번쨰 노드 삽입
    if head.data == findData :
        node = Node()
        node.data = data
        node.frontLink = head
        head.backLink = node
        head = node
        return dataArray

    #중간(cur과 prev 사이에 삽입)
    curPosition = head
    while curPosition.frontLink != None :
        prevNode = curPosition
        curPosition = curPosition.frontLink # 앞으로 한 칸 전진
        if curPosition.data == findData :
            node = Node()
            node.data = data
            node.frontLink = curPosition
            prevNode.frontLink = node
            curPosition.backLink = node
            node.backLink = prevNode
            return

    # 끝
    node = Node()
    node.data = data
    curPosition.frontLink = node
    node.backLink = curPosition

def deleteNode(data) :
    global head, memory, curPosition, prevNode
    # delNode = None # deleNode 메소드에서만 쓰는 변수
    # 첫번쨰 노드 삭제
    if head.data == data :
        curPosition = head
        head = head.frontLink
        del(curPosition)
        return

    # 중간 ~  끝
    curPosition = head
    while curPosition.frontLink != None :
        prevNode = curPosition
        curPosition = curPosition.frontLink
        if curPosition.data == data :
            # delNode = curPosition
            # curPosition = curPosition.frontLink # 한 칸 전진
            prevNode.frontLink = curPosition.frontLink # frontLink 연결
            curPosition.frontLink.backLink = prevNode # backLink 연결
            del(curPosition)
            return


def findNode(data) :
    global head, memory, curPosition, prevNode

    curPosition = head
    # 첫번째 노드
    if curPosition.data == data :
        return curPosition.data

    # 중간
    while curPosition.frontLink != None :
        curPosition = curPosition.frontLink
        if curPosition.data == data :
            return curPosition.data

    return None


# 출력하기
def printNode(start) :
    curPosition = start

    # 노드가 1개일 떄
    if curPosition.frontLink == None :
        return

    print("정방향 ---> ", end = ' ')
    print(curPosition.data, end = ' ')
    # 노드가 2개 이상일 때
    while curPosition.frontLink != None :
        curPosition = curPosition.frontLink
        print(curPosition.data, end = ' ')
    print()

    # 정방향을 다 돌면 curPosion은 마지막 노드에 가있다.
    print("역방향 ---> ", end = ' ')
    print(curPosition.data, end = ' ')
    while curPosition.backLink != None :
        curPosition = curPosition.backLink
        print(curPosition.data, end = ' ')
    print()
    print()


memory = []
head, curPosition, prevNode = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == '__main__' :

    # 첫번쨰 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 두번쨰 노드부터 끝까자
    for data in dataArray[1:] :
        prevNode = node
        node = Node()
        node.data = data
        prevNode.frontLink = node
        node.backLink = prevNode
        memory.append(node)

    print("일반 출력")
    printNode(head) # 굿

    print("insertNode 실행 후 출력 결과")
    insertNode("쯔위", "성호") # 굿
    printNode(head)

    print("deleteNode 실행 후 출력 결과")
    deleteNode("정연") # 굿
    printNode(head)

    fNode = findNode("성호") # 굿
    print("findeNode 출력 : ", fNode)
