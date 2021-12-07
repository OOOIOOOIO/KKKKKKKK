
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None


def printNode(start) :
    global head, curPosition, prevNode
    curPosition = start

    if curPosition.data == None :
        return

    print(curPosition.data, end = " ") #  첫번쨰 노드
    while curPosition.link != None :
        curPosition = curPosition.link
        print(curPosition.data, end = " ")
    print(); print()

def insertNode(findData, data) :
    global head, curPosition, prevNode
    if findData  == data :
        node = Node()
        node.data = data
        node.link = head
        head = node
        return

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

    # curPostion이 다 돌면 마지막 노드가 되는데ㅔ, 이 떄 findData를 못 찾으면 그냥 맨 마지막에 삽입한다. 추가한다는 개념
    node = Node()
    node.data = data
    curPosition.link = node




def deleteNode(findData) :
    global head, curPosition, prevNode
    if head.data == findData :
        curPosition = head
        head = head.link
        del(curPosition)
        return

    curPosition = head
    while curPosition.link != None :
        prevNode = curPosition
        curPosition = curPosition.link
        if curPosition.data == findData :
            prevNode.link = curPosition.link
            del(curPosition)
            return



def findNode(findData) :
    global head, curPosition, prevNode

    if head.data == findData :
        return head.data

    curPosition = head
    while curPosition.link != None :
        curPosition = curPosition.link
        if curPosition.data == findData :
            return curPosition.data

    return None


memory = []
head, curPosition, prevNode = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == '__main__' :

    node = Node()
    node.data = dataArray[0]
    head = node

    for data in dataArray[1:] :
        prevNode = node
        node = Node()
        node.data = data
        prevNode.link = node




    insertNode("정연", "성호")
    printNode(head)

    deleteNode("사나")
    printNode(head)

    # findNode는 리턴일 뿐이기에 print()를 해줘야한당 
    print(findNode("김성호"))
    printNode(head)
