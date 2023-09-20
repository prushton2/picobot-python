from picobot import move, get, state, setstate, stateFunctions
# This picobot relies on states to run, starting at state 0
# To define a state, create a function with a decorator of @state(<state id>)
# Include an argument for the canvas inside your state function, and include this as a parameter when calling
# a move or check function
# ex:
# @state(0)
# def state0fn():
#   move("N")
#   if(get("***S")):
#      setstate(1)

@state(0)
def s0f():
    move("S")
    if(get("***S")):
        setstate(1)


@state(1)
def s1f():
    move("W")
    if(get("**WS")):
        setstate(10)

