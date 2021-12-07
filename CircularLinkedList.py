class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

# 출력 함수
def printNode(start) :
    curPosition = start
    #노드가 비어있을 때
    if curPosition.link == None :
        return


    print(curPosition.link, end = " ") # 첫 노드 출력
    while curPosition.link != None :
        curPosition = curPosition.link
        print(curPosition.link, end = " ")
    print()


# 삽입 함수
def inserNode(findData, data) :
    global head, curPosition, prevNode, memory
    # 맨 앞에 삽입
    if head.data == findData :
        node = Node()
        node.data = data
        node.link = head
        lastNode = head # 마지막 노드를 찾기 위해 
        while lastNode.link != None :
            lastNode = lastNode.link
        lastNode.link = node
        head = node
        return
    # 중간에 삽입
    curPosition = head
    while curPosition.link != None :
        prevNode = curPosition
        curPosition = curPosition.link

        if curPosition.data == findData :
            node = Node()
            node.data = data
            node.link = curPosition
            prevNode.link = node
            return
    # 마지막에 삽입
    node = Node()
    node.data = data
    node.link = head
    curPosition.link = node


# 삭제 함수
def deleteNode(deleteData) :
    global head, curPosition, prevNode, memory
    # 맨 앞노드 삭제
    if head.data == deleteData :
        curPosition = head
        lastNode = head
        while lastNode.link != None :
            lastNode = lastNode.link
        lastNode.link = head.link
        head = head.link
        del(curPosition)
        return

    # 중간 ~ 끝 삭제
    curPosition = head
    while curPosition.link != None :
        prevNode = curPosition
        curPosition = curPosition.link
        if curPosition.data == deleteData :
            prevNode.link = curPosition.link
            del(curPosition)
            return


# 검색 함수
def findNode(findData) :
    global head, curPosition, prevNode, memory
    # 처음
    if head.data == findData :
        return head.data
    # 중간
    curPosition = head
    while curPosition.link != None :
        if curPosition.data == findData :
            return curPosition.data
    # 아무것도 없을 때
    return None


# 전역 변수
memory = []
head, curPosition, prevNode, = None, None, None
dataArr = ["다현", "정연", "쯔위", "사나", "지효"]


# 메인함수
if __name__ == '__main__' :

    # 우선 링크드리스트 구하기
    node = Node()
    node.data = dataArr[0]
    head = node
    node.link = head

    for data in data[1:] :
        prevNode = node
        node = Node()
        node.data = data
        prevNode.link = node
        node.link = head
        memory.append(node)


    printNode(head)

    insterNode(findData, data)

    deleteNode(deleteData)

    findNode(findData)
