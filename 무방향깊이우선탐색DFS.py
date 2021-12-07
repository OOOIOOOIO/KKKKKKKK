# 그래프 선언 및 행렬 만들기
class Graph() :
    def __init__(self, size) :
        self.size = size
        self.graph = [[0 for _ in range(self.size)] for _ in range(self.size)]





# 전역변수
G1 = None
stack = []  # 일단 방문한 노드 저장하고 이쪽저쪽 갔다 다시 원점으로 돌아오기 위한 스택
visitedNode = [] # 방문했는지 확인할 배열

if __name__ == '__main__':
    # 4*4행렬(그래프) 생성
    G1 = Graph(4)
    # 노가다로 넣기
    G1.graph[0][2] = 1; G1.graph[0][3] = 1;
    G1.graph[1][2] = 1;
    G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1;
    G1.graph[3][0] = 1; G1.graph[3][2] = 1;

    # 일단 행렬 출력
    print("*****G1 무방향 그래프*****")
    for row in range(G1.size) :
        for col in range(G1.size) :
            print(G1.graph[row][col], end = " ")
        print()

    # 시작 정점
    current = 0;
    stack.append(current)
    visitedNode.append(current)

    print("pop된 순서 -->", end=" ")

    while(len(stack) != 0) :
        nextNode = None
        for vertex in range(G1.size) : # 노드의 개수만큼
            if G1.graph[current][vertex] == 1 : # 현재노드와 연결이 되어 있다면
                if vertex in visitedNode : # 이미 방문한 노드라면
                    pass                # 다음노드로 그냥 넘어가기
                else :
                    nextNode = vertex
                    break # for문 끝내기

        # 다음 노드(아직 방문하지 않은 노드)가 있다면 그 노드를 현재 노드로 지정
        if nextNode != None :
            current = nextNode # current는 다음 노드()아직 방문하지 않은 노드)
            stack.append(current)
            visitedNode.append(current) # 방문 했으니 stack이랑 visitedNode에 넣어주기
        else :
            current = stack.pop() # 현재 노드에서  방문하지 않은 노드가 없다면(모두 방문했다면) .pop()을 통해 현재 노드를 다시 현재 노드로 지정하고 돌린다.
            print(chr(ord('A')+current), end=" ")      # 그럼 아마 다시 여기로 들어올텐, 이미 pop()해 현재 노드는 stack에 없는 상태니 이전 노드가 pop되고 이게 돌아돌아 stack의 길이는
                                # 줄어들어 언젠가 마지막 노드까지 .pop()되어 stack의 길이는 0이 될 것이고 while문을 탈출할 것이다.
    print()
    
    print("방문 순서 --->", end=" ")
    for i in visitedNode :
        print(chr(ord('A')+i), end=" ")
