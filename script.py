from picobot import move, state, stateFunctions
# This picobot relies on states to run, starting at state 0
# To define a state, create a function with a decorator of @state(<state id>)
# Include an argument for the canvas inside your state function, and include this as a parameter when calling
# a move or check function
# ex:
# @state(0)
# def state0fn(c):
#   move(c, N)
