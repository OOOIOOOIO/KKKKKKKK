# 이진탐색트리
class TreeNode() :
    def __init__(self) :
        self.data = None
        self.left = None
        self.right = None

# 재귀 함수 사용
# 전위 순회
def preorder(node) :
    if node == None :
        return
    print(node.data, end = " -> ")
    preorder(node.left)
    preorder(node.right)


# 중위 순회
def inorder(node) :
    if node == None :
        return
    inorder(node.left)
    print(node.data, end = " -> ")
    inorder(node.right)


# 후위 순회
def postorder(node) :
    if node == None :
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = " -> ")


# 이진탐색트리 만들기
def makeTree() :
    global root, arr, memory

    # 두번째부터 끝까지 추가, 하나씩 검사해서 트리 만들기
    for name in arr[1:] :

        node = TreeNode()
        node.data = name

        # main에서 root(첫번째 배열 요소) 넣어둠
        curPos = root

        while True :
            if name < curPos.data :  # root보다 작다면 왼쪽에 추가
                if curPos.left == None :
                    curPos.left = node
                    break
                curPos = curPos.left

            else :
                if curPos.right == None :  # root보다 크다면 오른쪽에 추가
                    curPos.right = node
                    break
                curPos = curPos.right

        memory.append(node)
    print("이진 탐색 트리 구성 완료")



# 데이터 삽입하기
def insertTree(name) :
    global root, arr, memory
    node = TreeNode()
    node.data = name
    # flagleft = False
    # flagright = False
    curPos = root
    while True :
        if name < curPos.data :  # root보다 작다면 왼쪽에 추가
            if curPos.left == None :
                # flagleft = True
                # beforeNode = curPos.left
                curPos.left = node
                break
            curPos = curPos.left

        else :
            if curPos.right == None :  # root보다 크다면 오른쪽에 추가
                # flagright = True
                # beforeNode = curPos.right
                curPos.right = node
                break
            curPos = curPos.right
    # if flagleft :
    #     insertTree(beforeNode.data)
    # if flagright :
    #     insertTree(beforeNode.data)

    memory.append(node)

# 데이터 삭제하기
def deleteTree(deleteName) :
    global root, arr, memory

    curPos = root
    parent = None

    # 삭제할 데이터가 root 데이터인 경우???

    while True :
        # 삭제할 데이터가 있는 경우
        if deleteName == curPos.data :
            # 삭제하려는 노드의 자식들이 없는 경우(리프 노드)
            if curPos.left == None and curPos.right == None :
                if parent.left == curPos :
                    parent.left = None
                else :
                    parent.right = None
                print("blah1")
                del(curPos)

            # 삭제하려는 노드의 자식이 left만 존재할 경우
            elif curPos.left != None and curPos.right == None :
                if parent.left == curPos : # curPos가 왼쪽인지 오른쪽인지 검사
                    parent.left = curPos.left
                else :
                    parent.right = curPos.left
                print("blah2")
                del(curPos)

            # 삭제하려는 노드의 자식이 right만 존재할 경우
            elif curPos.left == None and curPos.right != None :
                if parent.left == curPos :
                    parent.left = curPos.right
                else :
                    parent.right = curPos.right
                print("blah3")
                del(curPos)

            # 둘 다 존재할 경우는?????
            print(deleteName, "이(가) 삭제됨")
            break



        # 삭제할 데이터가 없는 경우 어차피 맨 처음 root를 거치기 대문에 삭제할 데이터가 없기에
        # 여기서 시작을 parent = current(root)로 지정해준다. 이후에 쭉쭉 parent를 지정해준다.
        elif deleteName < curPos.data : # 없는 경우에서 루트보다 더 작을 경우
            if curPos.left == None :
                print(deleteName, "이(가) 존재하지 않음")
                break
            parent = curPos
            curPos = curPos.left

        else :
            if curPos.right == None : # 없는 경우에서 루트보다 더 클 경우
                print(deleteName, "이(가) 존재하지 않음")
                break
            parent = curPos
            curPos = curPos.right


# 데이터 검색하기
def findTree(findName) :
    global root, arr, memory

    curPos = root
    while True :
        if findName == curPos.data :
            print(findName, "을(를) 찾음")
            break

        elif findName < curPos.data :
            if curPos.left == None :
                print(findName, "이(가) 존재하지 않음")
                break
            curPos = curPos.left
        else :
            if curPos.right == None :
                print(findName, "이(가) 존재하지 않음")
                break
            curPos = curPos.right


# 교수님이 하신 데이터 검색하기
def findTree2(findName, root) :
    global arr, memory

    if root == None :
        return print("찾고자 하는 값이 존재하지 않습니다.")

    if findName == root.data :
        return print(root.data,"를 찾았습니다.")

    elif findName < root.data :
        return findTree2(findName, root.left)

    else :
        return findTree2(findName, root.right)




# 전역변수
# arr = ["화사", "솔라", "문별", "휘인", "쯔위", "선미", "성호"]
arr = [5, 9, 6, 2, 4, 7, 1, 3, 10]
memory = []
root = None



if __name__ == '__main__':

    # 첫번째 추가해면서 시작
    node = TreeNode()
    node.data = arr[0]
    root = node
    memory.append(node)

    # 완전 이진 트리 구현
    makeTree()
    print()

    # 전위 순회로 출력해보기
    print("preorder : ", end = "")
    preorder(root)
    print("끝")
    print()

    # 중위 순회
    print("inorder : ", end = "")
    inorder(root)
    print("끝")
    print()

    # 후위 순회
    print("postorder : ", end = "")
    postorder(root)
    print("끝")
    print()

    # 삽입 후 출력해보기
    # insertTree("김성호")
    insertTree(3.5)
    print("insertTree 후 출력: ", end = "")
    preorder(root)
    print("끝")
    print()

    # 검색하기--> 이진 탐색 트리일 / 완전 이진 탐색일 경우 에러
    findTree(3)
    print()
    findTree2(100, root)
    print()

    # 삭제 후 출력해보기
    deleteTree(5) # 1인 경우 parent가 None이라서 에러, 5인 경우 left, right가 있어서 에러
    print()
    print("deleteTree 후 출력: ", end = "")
    preorder(root)
    print("끝")
    print()
