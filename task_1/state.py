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
import copy


def create(l):
    return[l+[0],[],[]]

#Returns a list of states one cross away from state x (the children of x)
def get_next(x):
    """
    Takes the current state of the game as input and returns a list of all possible next states of the game.
    The game state is represented by a list x of three sublists:
    - The first sublist represents the left bank of a river and contains integers representing the weights of different objects present on the left bank.
    - The second sublist represents the right bank of the river and contains integers representing the weights of different objects present on the right bank.
    - The third sublist represents the history of moves made so far and contains sublists representing the moves made in the form [left_bank_objects, right_bank_objects].
    """
    # Create an empty list to store the possible next states
    final_list = []

    # Check if 0 is present in the left bank
    if 0 in x[0]:
        # If 0 is present, remove it from the left bank
        x[0].remove(0)
        # Iterate over all possible pairs of objects on the left bank
        for i in range(0, len(x[0]) - 1):
            counter = 1 + i
            while counter < len(x[0]):
                # Get the values of the two objects in the pair
                first_val = x[0][i]
                second_val = x[0][counter]
                # Create a deep copy of the current state
                temp = copy.deepcopy(x)
                # Remove the two objects from the left bank of the copied state
                temp[0].remove(first_val)
                temp[0].remove(second_val)
                # Add the two objects and the boat to the right bank of the copied state
                temp[1].append(first_val)
                temp[1].append(second_val)
                temp[1].append(0)
                # Add the move to the history of moves made so far
                temp[2].append([first_val, second_val])
                # Add the copied state to the list of possible next states
                final_list.append(temp)
                counter = counter + 1
    else:
        # If 0 is not present in the left bank, check if the left bank is empty
        if not x[0]:
            # If the left bank is empty, return the input state
            return [x]
        # If the left bank is not empty, remove 0 from the right bank
        x[1].remove(0)
        # Iterate over all objects on the right bank
        for i in range(0, len(x[1])):
            # Create a deep copy of the current state
            temp = copy.deepcopy(x)
            # Remove the object from the right bank of the copied state
            val = x[1][i]
            temp[1].remove(val)
            # Add the object and the boat to the left bank of the copied state
            temp[0].append(val)
            temp[0].append(0)
            # Add the move to the history of moves made so far
            temp[2].append([val, 0])
            # Add the copied state to the list of possible next states
            final_list.append(temp)

    # Return the list of possible next states
    return final_list
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

