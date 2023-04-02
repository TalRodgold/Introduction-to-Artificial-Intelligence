'''
The state is a list of three items:
1. Who is on the left side? each person is represented by its crossing time. 0=flashlight
2. Who is on the right?
3. A list of moves. Every move is a list the persons(crossing times)
   that crossed the bridge
start: all people on the left side
target: all people on the right
'''


#l is a list of the crossing times. the init. state is a list of crossing times
#+ 0 for the flashlight (all initially on the left side),
#and empty list=pers on the right and another empty list=moves so far.
def create(l):
    return[l+[0],[],[]]

#Returns a list of states one cross away from state x (the children of x)
def get_next(x):

    # your code here
    if len(x[0]) == 0:
        return [x]
    if 0 in x[0]: # if flashlight on left side
        x[0].remove(0)  # remove flashlight
        shortest = min(x[0])    # get the person that crosses the bridge in the shortest time
        x[0].remove(shortest)  # remove person that crosses the bridge in the shortest time
        cross = x[0][0] # get first person in list to cross with shortest
        x[0].remove(cross)   # remove first person in list to cross with shortest
        x[1].append(shortest)
        x[1].append(cross)
        x[1].append(0)  # add flashlight to left side
        x[2].append(cross)
        return [x]
    # if flashlight on right side
    x[1].remove(0)  # remove flashlight
    shortest = min(x[1])  # get the person that crosses the bridge in the shortest time
    x[1].remove(shortest)  # remove person that crosses the bridge in the shortest time
    x[0].append(shortest)
    x[0].append(0)  # add flashlight to left side
    x[2].append(shortest)
    return [x]

#Gets x (a state) and returns the length of the path to that state.
def path_len(x):
    pl=0           #pl sums the path length
    for i in x[2]: #for all the moves:
        pl+=max(i) #  sum into pl the max. crossing time of the 1 or 2 pers. crossing
    return pl

#returns True iff state x is the target.
#x is the target iff no one is on the left side.
def is_target(x):
    return x[0]==[]

def hdistance(s):
    if s[0] == []:
        return 0                   # the heuristic value of s
    h = 0
    x = sorted(s[0])
    if x[0] == 0:
        x = x[1:]
    for i in range(len(x)-1, -1, -2):
        h += x[i]
    return h

