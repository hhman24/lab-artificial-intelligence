
def readFile(nameFile):
    vertices = 0
    src = 0
    des = 0
    option = 0
    matrix = []
    heuristic = [] 

    with open(nameFile, 'r') as f:
        line = f.readline() # đọc kí số lượng vertex
        vertices = int(line)

        l = f.readline() # đọc yêu cầu bài toán
        tmp = l.split()
        src = int(tmp[0])
        des = int(tmp[1])
        option = int(tmp[2])

        for i in range(vertices): # đọc ma trận
            line = f.readline()
            t = [int(l.strip()) for l in line.split(' ')] # split() tac chuoi theo dk, strip xoa khoang trang
            matrix.append(t)

        line = f.readline()

        heuristic = [int(l.strip()) for l in line.split(' ')]

        f.close()

    return vertices, src, des, option, matrix, heuristic

def writeFile(fileName, expandedList, path):
    with open(fileName, 'w+') as f:
        for i in expandedList:
            f.write(str(i._name))
            f.write(" ")

        f.write("\n")
        for i in path:
            f.write(str(i._name))
            f.write(" ")

        if(path == []):
            f.write("No path.")

        f.close()



