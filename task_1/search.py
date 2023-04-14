#search
import task_1.state as state
import task_1.frontier as frontier

# The heuristic transfers the people across in the least amount of time possible.
# And that is exactly the reason why it is acceptable, since it will always give us the least
# amount of time possible for any scenario.

def search(n):
    s=state.create(n)
    f=frontier.create(s)
    # The code does not present how the list X looks after every step,
    # so I changed the code a little in order for us to see a detailed step by step.
    # Now, every time a couple went along the bridge we can see who is on the left, who is on the right
    # and which couples have went back and forth so far.
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        print(s)
        f = frontier.create(s)
        frontier.remove(f)
        if state.is_target(s):
            return s
        ns=state.get_next(s)
        for i in ns:
            if state.is_target(i):
                return i
            frontier.insert(f,i)
    return 0



print(search([1,2,5,10]))
