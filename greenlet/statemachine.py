from greenlet import greenlet

state = 'FIRST'



def from_first_to_second():
    global state
    next_greenlet = state_machine[state]
    state = 'SECOND'
    print("Moved to %s" % state)
    next_greenlet.switch()

def from_second_to_third():
    global state
    next_greenlet = state_machine[state]
    state = 'THIRD'
    print("Moved to %s" % state)
    next_greenlet.switch()

def from_third():
    print("Got to third")


def main():
    global state
    global state_machine
    global gr1, gr2, gr3


    gr1 = greenlet(from_first_to_second)
    gr2 = greenlet(from_second_to_third)
    gr3 = greenlet(from_third)

    state_machine = {
        'FIRST': gr2,
        'SECOND': gr3
    }


    gr1.switch()

if __name__ == "__main__":
    main()

