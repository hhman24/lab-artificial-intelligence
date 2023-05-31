import copy
import heapq

"""
    Data structure Vertex, 
    """
class Vertex:
    def __init__(self, _name, _heuristic):
        self._name =  _name
        self._heuristic = _heuristic

    def __repr__(self):
        return f"{self._name}"

    def __lt__(self, other):
        if(self._name < other._name):
            return True
        else:
            return False
        
class G:

    __vertexs = list() # list of vertex
    __matrix = list() # Adjacent Matrix 

    def __init__(self, _numOfVertex, _matrix, _heuristic):
        """
        Contructor Function:
            input:  _numOfVertex: number of vertex from input file
                    _matrix: adjacent matrix from input file
                    _heuristic: list of heuristic from input file
        """
        self.__numOfVertex = _numOfVertex
        self.__matrix = copy.deepcopy(_matrix)
        self.add_list_vertex(_heuristic)
        
    def add_list_vertex(self, _heuristic):
        """
            contructor list of vertex with heristc
            """
        for i in range(len(_heuristic)):
            v = Vertex(i, _heuristic[i])
            self.__vertexs.append(v)

    def bfs(self, src, des):
        frontier = []
        expandedList = [] 
        visited = {} # store path with key is node value is parent
        path = list()
        isGoal = False

        if(src == des):
            path.append(self.__vertexs[src])
            return expandedList, path

        frontier.append(self.__vertexs[src])
        while(frontier != []):
            if(isGoal):
                break

            node = frontier.pop(0)
            expandedList.append(node)
            for i in range(self.__numOfVertex):
                valueChild = self.__matrix[node._name][i]
                if(valueChild != 0):
                    childNode = self.__vertexs[i]
                    if((childNode not in expandedList) and (childNode not in frontier)):
                        visited[childNode] = node
                        if(childNode._name == des):
                            isGoal = True
                            break

                        frontier.append(childNode)

        path = self.found_Path(visited, src, des)

        return expandedList, path

    def __recursion_dfs(self, exList, visited, src, des):
        if(src ==  des):
            visited.append(src)
            return True

        visited.append(src)
        exList.append(src)
        
        for i in range(self.__numOfVertex):

            if((self.__matrix[src._name][i] != 0)):

                node = self.__vertexs[i]
                if(node  in visited):
                    continue

                goal = self.__recursion_dfs(exList, visited, node, des)

                if(goal != False):
                    return True


        visited.pop()

        return False

    def dfs(self, src, des):
        visited = []
        expandedList = []

        if(src == des):
            visited.append(self.__vertexs[src])
            return expandedList, visited

        self.__recursion_dfs(expandedList, visited, self.__vertexs[src], self.__vertexs[des])
        return expandedList, visited

    def __cost_path(self, val): # use for function for sort(key=) assignment element 
        return val[0]

    def ucs(self, src, des):
        frontier = [] 
        expandedList = []
        path = []
        visited = {}  # store path with key is node value is parent
        pathCost = 0 

        if(src == des):
            path.append(self.__vertexs[src])
            return expandedList, path

        frontier.append([0, self.__vertexs[src]])
        while (frontier != []):
            frontier.sort(key= self.__cost_path)
            node = frontier.pop(0)
            pathCost = node[0]
            if(node[1]._name == self.__vertexs[des]._name):
                expandedList.append(node[1])
                break

            expandedList.append(node[1])
            for i in range(self.__numOfVertex):
                valueChild = self.__matrix[node[1]._name][i]
                if(valueChild != 0):
                    childNode = self.__vertexs[i]
                    isNotIn = True
                    index = 0
                    for f in frontier:
                        if(f[1]._name == childNode._name):
                            isNotIn = False
                            break

                        index += 1

                    if((childNode not in expandedList) and isNotIn):    
                        visited[childNode] = node[1]
                        frontier.append([pathCost + valueChild,childNode])
                    elif(not isNotIn and frontier[index][0] > pathCost + valueChild):
                        visited[childNode] = node[1]
                        frontier[index][0] = pathCost + valueChild

        path = self.found_Path(visited, src, des)
        return expandedList, path

    def __dls(self, exList, visited, src, des, limit):
        if(src ==  des):
            visited.append(src)
            return True
        elif(limit == 0):
            visited.append(src)
            exList.append(src)
            return "cutoff"
        else:
            cutoff_occurred = False

        visited.append(src)
        exList.append(src)
        
        for i in range(self.__numOfVertex):

            if((self.__matrix[src._name][i] != 0)):

                node = self.__vertexs[i]
                if(node  in visited):
                    continue

                goal = self.__dls(exList, visited, node, des, limit - 1)

                if(goal == True):
                    return True
                elif(goal == 'cutoff'):
                    cutoff_occurred = True
                    visited.pop()

        if cutoff_occurred:
            return 'cutoff'
        else:
            return False
 
    def ids(self, src, des):
        visited = []
        expandedList = []
        d = 0
        while(True):
            if(self.__dls(expandedList, visited, self.__vertexs[src], self.__vertexs[des], d) == 'cutoff'):
                expandedList = []
                visited = []
            else:
                break
            d+=1

        return expandedList, visited

    def gbfs(self, src, des):
        expandedList = []
        visited = {} # store path with key is node value is parent
        frontier = [] # element frontier is (heristic, node, parent node)
        path = []
        isGoal = False

        if(src == des):
            path.append(self.__vertexs[src])
            return expandedList, visited

        frontier.append((0 , self.__vertexs[src], self.__vertexs[src])) # (h, node, parent)
        while(frontier != []):
            if(isGoal):
                break

            heapq.heapify(frontier)
            (hNode, node, parent) = heapq.heappop(frontier)
            expandedList.append(node)
            visited[node] = parent
            
            while(1):
                open_list = []
                for i in range(self.__numOfVertex):
                    
                    value_child = self.__matrix[node._name][i]
                    child_node = self.__vertexs[i]
                    if(value_child != 0):
                        if(child_node is self.__vertexs[des]):
                            visited[child_node] = node
                            isGoal = True
                            break

                        is_in = False
                        for f in frontier: 
                            if f[1] is node:
                                is_in = True

                        if(child_node not in expandedList and is_in is False): # and is_in is False
                            open_list.append((child_node._heuristic, child_node, node))

                if(isGoal):
                    break

                if(open_list == []):
                    break
                heapq.heapify(open_list)
                (hNode, node, parent) = heapq.heappop(open_list)
                visited[node] = parent
                expandedList.append(node)
                frontier += open_list
                    
        path = self.found_Path(visited, src, des)
        return expandedList, path     

    def Astart(self, src, des):
        expandedList = []
        visited = {} # store path with key is node value is parent
        frontier = [] 
        path = []


        if(src == des):
            path.append(self.__vertexs[src])
            return expandedList, visited

        frontier.append((0 , self.__vertexs[src], 0, self.__vertexs[src])) # (f, node, g, parent)
        while(frontier != []):

            heapq.heapify(frontier)
            (f, node, g_path_cost, parent) = heapq.heappop(frontier)
            if(node in expandedList):
                continue

            expandedList.append(node)
            visited[node] = parent
            if(node == self.__vertexs[des]):
                break

            for i in range(self.__numOfVertex):
                g_child = self.__matrix[node._name][i]
                child_node = self.__vertexs[i]
                if(g_child != 0):
                    g_child += g_path_cost
                    f_child = child_node._heuristic + g_child

                    if(child_node not in expandedList):
                        frontier.append((f_child, child_node, g_child, node))
                    
        path = self.found_Path(visited, src, des)
        return expandedList, path

    def hc(self, src, des):
        expandedList = []
        path = []
        
        if(src == des):
            path.append(self.__vertexs[src])
            return expandedList, path
        current_node = self.__vertexs[src]

        old_state = None
         
        while(old_state != current_node):
            path.append(current_node)
            expandedList.append(current_node) 
            successor = current_node
            old_state = current_node
            for i in range(self.__numOfVertex):
                if(self.__matrix[old_state._name][i] != 0):
                    new_state = self.__vertexs[i]  
                    if(self.__vertexs[i] == self.__vertexs[des]):
                        path.append(self.__vertexs[i])
                        return expandedList, path
                    
                    if(new_state._heuristic < successor._heuristic):
                        successor = new_state
                    
                    if(successor._heuristic < current_node._heuristic):
                        current_node = successor

        if(len(path) <= 1):
            path = []
        return expandedList, path

    def found_Path(self, visited, src, des):
        path = []
        try:
            path.insert(0, self.__vertexs[des])
            nextNode =  self.__vertexs[des]    
            while self.__vertexs[src] not in path:
                try:
                    prevNode = visited[nextNode]
                    path.insert(0, prevNode)
                    nextNode = prevNode
                    
                except:
                    print("Not to found path from ", src, " to ", des)
                    break 
            
            if len(path) <= 1:
                path = []
            return path        
        except:
            pass

