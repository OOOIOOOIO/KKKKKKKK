# 그래프 선언 및 행렬 만들기
class Graph() :
    def __init__(self, size) :
        self.size = size
        self.graph = [[0 for _ in range(self.size)] for _ in range(self.size)]

# 출력
def printGraph(g) :
    print(" ", end=" ")
    for i in range(g.size) :
        print(nameAry[i], end=" ")
    print()
    for row in range(g.size) :
        print(nameAry[row], end=" ")
        for col in range(g.size) :
            print(g.graph[row][col], end=" ")
        print()
    print()

def findVertex(g, findVtx) :
    stack = []
    visitedAry = []

    #시작 노드
    current = 0

    stack.append(current)
    visitedAry.append(current)

    while(len(stack) != 0) :
        next = None
        for vertex in range(6) :
            if g.graph[current][vertex] != 0 :
                if vertex in visitedAry :
                    pass
                else :
                    next = vertex
                    break
        if next != None :
            current = next
            stack.append(current)
            visitedAry.append(current)
        else :
            current = stack.pop()
    if findVtx in visitedAry :
        return "있음"

    else :
        return "없음"


# 전역변수
G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5


if __name__ == '__main__':

    gSize = len(nameAry)
    G1 = Graph(gSize)
    G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1;
    G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1;
    G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1;
    G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1; G1.graph[쯔위][화사] = 1;
    G1.graph[선미][쯔위] = 1; G1.graph[선미][화사] = 1;
    G1.graph[화사][쯔위] = 1; G1.graph[화사][선미] = 1;


    print("****G1 무방향 그래프***")
    printGraph(G1)

    result = findVertex(G1, 쯔위)
    print(result)
