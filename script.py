from picobot import move, state, stateFunctions
# This picobot relies on states to run, starting at state 0
# To define a state, create a function with a decorator of @state(<state id>)
# ex:
# @state(0)
# def state0fn():
#   move(N)
