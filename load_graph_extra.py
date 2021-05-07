# name: Kevin Lin
# date: 03/12/21
# purpose: load information from a .txt file into a list or dictionary

from vertex_extra import Vertex

# Parameters: file is a .txt file
# loads information from a .txt file into a dictionary and returns that dictionary
def load_graph(file):
    vertex_dict = {}

    # fills vertex_dict with keys and values corresponding to a vertex name and the vertex object
    info_file = open(file, "r")
    for line in info_file:
        temp_list = line.split(";")

        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i].strip()

        adj_list = temp_list[1].split(",")
        for x in range(len(adj_list)):
            adj_list[x] = adj_list[x].strip()

        xy_list = temp_list[2].split(",")
        for y in range(len(xy_list)):
            xy_list[y] = xy_list[y].strip()

        v = Vertex(temp_list[0], xy_list[0], xy_list[1])
        vertex_dict[temp_list[0]] = v

    info_file.close()


    # fills in the adj_list of each object with a list of adjacent objects
    info_file = open(file, "r")
    for line in info_file:
        temp_list = line.split(";")

        adj_list = temp_list[1].split(",")
        for x in range(len(adj_list)):
            adj_list[x] = adj_list[x].strip()

        v = vertex_dict[temp_list[0]]

        for name in adj_list:
            object = vertex_dict[name]
            v.adj_list.append(object)

    info_file.close()

    return vertex_dict

# Parameters: file is a .txt file
# loads information from a .txt file into a list and dictionary and returns that list
def load_list(file):
    vertex_list = []
    vertex_dict = {}
    line_no = 0

    # fills vertex_dict with keys and values corresponding to a vertex name and the vertex object
    info_file = open(file, "r")
    for line in info_file:
        temp_list = line.split(";")

        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i].strip()

        adj_list = temp_list[1].split(",")
        for x in range(len(adj_list)):
            adj_list[x] = adj_list[x].strip()

        xy_list = temp_list[2].split(",")
        for y in range(len(xy_list)):
            xy_list[y] = xy_list[y].strip()

        v = Vertex(temp_list[0], xy_list[0], xy_list[1])
        vertex_list.append(v)
        vertex_dict[temp_list[0]] = v   # add information to a dictionary so filling in the adj_list still works

    info_file.close()


    # fills in the adj_list of each object with a list of adjacent objects
    info_file = open(file, "r")
    for line in info_file:
        line_no = line_no + 1
        temp_list = line.split(";")

        adj_list = temp_list[1].split(",")
        for x in range(len(adj_list)):
            adj_list[x] = adj_list[x].strip()

        for name in adj_list:
            object = vertex_dict[name]
            vertex_list[line_no-1].adj_list.append(object)

    info_file.close()

    return vertex_list
