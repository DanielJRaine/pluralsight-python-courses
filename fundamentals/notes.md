// 3.3 is the version of this course

__foo__ is pronounced "dunder foo"
debugging
unit testing
module creation and export

modules
-------
package is a module that can contain other modules and/or packages
packages are represented by directories.
modules are generally single files.

sys.path is a list of directories.

creating packages:
    - create the package somewhere in sys.path
    - create a file called __init__.py
    - this is called the package init file and turns the directory into a package.

LEGB scope lookup rule
1. Local
2. Enclosing
3. Global - use global keyword to use global variables
4. Built-ins

type
dir() introspects an object
__name__ for an object's name
__doc__ for an object's docs

tuple: immutable sequence of arbitrary objects t = ("Norway", 4.95, 3)
    - single element tuple declared as (391,) with trailing comma.
    - empty_tuple = ()
    - Python can infer to create a tuple from a comma separated series
    - iterable
    - can have nested tuples
    - access as with dictionaries
    - tuple unpacking: (allows multiple assignment with multiple return values)
        lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
        >>> lower
        31
        >>> upper 
        86
    - tuple([13, 2323, 44]) # tuple constructor
    - tuple(["Carmichael"]) # tuple constructor 
    >>> ('C','a','r'...)
range
set

str
    - join is more efficient than + for strings
    - "_" underscore is used for empty or dummy values, as an unwritten convention
        - many programs ignore warnings for missing values when underscore is used.
    - formatting:
        - "current position {latitude} {longitude}".format(latitude="60N", longitude="5E")
        - "current position {} {}".format("60N","5E") # used only once, same order as args
        - "current position {0} {1}".format("60N","5E") # indexed args, can be repeated
        >>> import math
        >>> "Math constants: pi={m.pi}, e={m.e}".format(m=math)

range([start], stop, [step])
    - stop value is one-past-the-end
    - "half-open"
    - ranges are not widely used in modern python code 

prefer enumerate() for counters
enumerate() yields (index, value) tuples
    - often combined with tuple unpacking

list
    - can be indexed from the end
    - negative indexing is essentially '-1' indexed rather than 0 indexed, so calculate accordingly
    - slice = seq[start:stop]
    - head, tail = seq[:3], seq[3:]

Collection Protocols
- Container
- Sized
- iterable
- sequence
- mutable sequence
- mutable set 
- mutable mapping     

raise 
handle
unhandled
exception objects

try:
    os.chdir(path)
    os.mkdir(dir_name)
except OSError as err:
    print(e, file=sys.stderr)
    raise
finally:
    os.chdir(original_path)


EAFP: Easier to ask forgiveness than permission (as opposed to look before you leap)

Laziness and the infinite
- just in time computation
- infinite (or large) sequences
    - sensor readings
    - mathematical series
    - massive files

generator comprehension (expression)
(expr(item) for item in iterable)

million_squares = (x*x for x in range(1, 1000001))

generators are single use objects

sum(x*x for x in range(1, 1000001))

sum(x for x in range(1001) if is_prime(x))

check out the itertools module


Tell objects what to DO
Don't ask them for their STATE

with-block (replaces a complex mess of try except and finally logic)
used with objects that return a context manager (such as open() in the file class)
the with construct will call file.close() for us implicitly even if we don't tell it to.
