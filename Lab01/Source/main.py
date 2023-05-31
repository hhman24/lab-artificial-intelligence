"""
    Hoang Huu Minh An
    ID: 20127102

    Lab01: Search strategies
        BFS, DFS, UCS, IDS, GBFS, AStart, HC
    """

from graph import G
import file
import requirement_input as ri
import sys

if __name__ == '__main__':
    """
        Argument from command line: `python main.py <input_file_path>`
    """
    if (len(sys.argv) != 2):
        raise Exception("Wrong input!!!")

    input = str(sys.argv[1])
    vertice, ri.SOURCE_NODE , ri.DESTINATION_NODE, o, m, h = file.readFile(input)
    msg = ri.STRATEGY_SEARCH[o]
    expanded_list = []
    path = []
    g = G(vertice, m, h)

    if(msg == "BFS"):
        expanded_list, path = g.bfs(ri.SOURCE_NODE, ri.DESTINATION_NODE)
    elif(msg == "DFS"):
        expanded_list, path = g.dfs(ri.SOURCE_NODE, ri.DESTINATION_NODE)
    elif(msg == "UCS"):
        expanded_list, path = g.ucs(ri.SOURCE_NODE, ri.DESTINATION_NODE) 
    elif(msg == "IDS"):
        expanded_list, path = g.ids(ri.SOURCE_NODE, ri.DESTINATION_NODE)
    elif(msg == "GBFS"):
        expanded_list, path = g.gbfs(ri.SOURCE_NODE, ri.DESTINATION_NODE)
    elif(msg == "AStar"):
        expanded_list, path = g.Astart(ri.SOURCE_NODE, ri.DESTINATION_NODE)
    elif(msg == "HC"):
        expanded_list, path = g.hc(ri.SOURCE_NODE, ri.DESTINATION_NODE)

    file.writeFile("output.txt", expanded_list, path)
 