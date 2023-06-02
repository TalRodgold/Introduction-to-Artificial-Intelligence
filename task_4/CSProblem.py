# BY: Tal Rodgold & Binyamin Mor
# ID: 318162344 & 317510485


# Graph Colouring
import math

# The graph is represented by a list with an item for every node.
# Item i represents node i+1 (the nodes are positive integers.)
# Each node is represented by a list of 3 items:
#   The color of the node (1...N). 0 for no color (yet)
#   A list of the node's neighbors (positive integers)
#   The domain -  a list of integers (1...N)
N = 0  # The colours are numbered 1...N


def create(fpath="graph.txt"):
    # fpath first line contains the num. of colours to be used.
    # The second line contains the list of neighbours of node 1.
    # The third line contains the list of neighbours of node 2.
    # ...
    global N
    p = []
    f = open(fpath, "r")
    N = int(f.readline())
    s = f.readline()
    while s != "":
        p += [[0, [int(i) for i in s.split()], list(range(1, N + 1))]]
        s = f.readline()
    f.close()
    present(p)
    return p


def domain(problem, v):
    # Returns the domain of v
    return problem[v - 1][2][:]


def domain_size(problem, v):
    # Returns the domain size of v
    return len(problem[v - 1][2])


def assign_val(problem, v, x):
    # Assigns x in var. v
    problem[v - 1][0] = x


def get_val(problem, v):
    # Returns the val. of v
    return problem[v - 1][0]


def erase_from_domain(problem, v, x):
    # Erases x from the domain of v
    problem[v - 1][2].remove(x)


def get_list_of_free_vars(problem):
    """
    Returns a list of variables that were not assigned a value.

    Args:
        problem (list): The problem representation.

    Returns:
        list: A list of variables that have not been assigned a value.
    """
    free_vars = []
    for i, node in enumerate(problem):
        if node[0] == 0:
            free_vars.append(i + 1)
    return free_vars


def is_solved(problem):
    # Returns True iff the problem is solved
    for i in problem:
        if i[0] == 0:
            return False
    return True


def is_consistent(problem, v1, v2, x1, x2):
    """
    Checks if assigning x1 to v1 and x2 to v2 is consistent.

    Args:
        problem (list): The problem representation.
        v1 (int): Variable v1.
        v2 (int): Variable v2.
        x1 (int): Value x1 assigned to v1.
        x2 (int): Value x2 assigned to v2.

    Returns:
        bool: True if the assignment is consistent, False otherwise.
    """
    if x1 == x2:
        return False
    neighbors_v1 = problem[v1 - 1][1]
    if v2 in neighbors_v1 and x2 == x1:
        return False
    return True


def list_of_influenced_vars(problem, v):
    """
    Returns a list of variables influenced by var v that still have no color.

    Args:
        problem (list): The problem representation.
        v (int): Variable v.

    Returns:
        list: A list of influenced variables that still have no color.
    """
    influenced_vars = []
    for neighbor in problem[v - 1][1]:
        if problem[neighbor - 1][0] == 0:
            influenced_vars.append(neighbor)
    return influenced_vars


def present(problem):
    for p in problem:
        print(p)
    print("************")
