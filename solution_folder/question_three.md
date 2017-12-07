Explain the difference of the floor and ceiling function. Can you think of a situation where you would use one or the other? Are they interchangable?

First, `math.ceil` and `math.floor` are not interchangable.  The former rounds up while the latter rounds down.  Thus your result will be different by some fraction, depending on which function you use.  You can probably use either function interchangably.  However, you should be consistent - if you round all your floats to int's you should consistently round up or down.  The `math.ceil` and `math.floor` functions allow you the level of control necessary to be consistent.

As a counter example, you might have the following situation:

list_of_floats = [0.1, 0.2, 0.5]
list_of_ints = [int(elem) for elem in list_of_floats]

The above certainly accomplishes the task of getting integers instead of floats, but it is not explicit in which choice is being made.  And the developer may not in fact what all the numbers to go one way or the other.  So for instance, say you want to sum all the ints, if the `int` function rounds down, then the sum is zero.  If the int function rounds, up then the sum is one.  And it is unclear from the code, which way you will round.

So in conclusion.  You get more control and granularity by using `math.ceil` and `math.floor`