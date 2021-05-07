# name: Kevin Lin
# date: 03/12/2021
# purpose: create dartmouth_alpha.txt

from quicksort import *
from load_graph_extra import *

search_list = load_list("dartmouth_graph.txt")

# Parameter: file is the name of a .txt file to be written on
# writes out a file containing dartmouth_graph.txt information but sorted
def write_output(file):
    sorted_dartmouth = open(file, "w")

    for i in range(0, len(search_list)):
        adj = []
        empty = ""
        for x in range(0, len(search_list[i].adj_list)):
            adj.append(search_list[i].adj_list[x].name)
            if x != len(search_list[i].adj_list)-1:
                adj.append(", ")
        adj_string = empty.join(adj)
        sorted_dartmouth.write(str(search_list[i]) + "; " + adj_string + "; " + str(search_list[i].x) + ", " + str(search_list[i].y) + "\n")

    sorted_dartmouth.close()

# Parameters: Both a and b are strings
# compares the ACSII values of two a and b and returns false if a is greater, else true
def compare_alpha(a, b):
    return a.name <= b.name

# Parameters: the_list is a list of vertex objects, compare_func is a function
# sorts the_list # - A - Z and writes it in dartmouth_alpha.txt
def sort_alpha(the_list, compare_func):
    sort(the_list, compare_func)
    write_output("dartmouth_alpha.txt")


sort_alpha(search_list, compare_alpha)
