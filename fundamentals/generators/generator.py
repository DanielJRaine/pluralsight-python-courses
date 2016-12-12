# specify iterable sequences
#   all generators are iterators

# are lazily evaluated
#   the next value in sequence is computed on demand

# can model infinite sequences
#   such as data streams with no definite end

# are composable into pipelines
#   for natural stream processing

# uses yield keyword at least once
# implicit return at end of function


def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()


next(g)
next(g)
next(g)



