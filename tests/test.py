# Global assignments
a = 5  # unused
b = 10 # used later
c = "test"  # unused
d = 20  # used in function
e = 50  # unused

def foo(x, y, z):
    x = 100  # reassigned, but used later
    m = 200  # unused
    n = x + y
    o = 0  # unused
    return n

def bar():
    p = 1  # unused
    q = 2  # used inside loop
    for i in range(5):
        print(q)

    r = 3  # unused
    s = "hello"  # unused
    t = s + " world"  # used

def baz():
    temp = 123
    temp2 = 456  # unused
    print("temp is", temp)

# Tuple unpacking (could break basic analyzers)
x, y = (1, 2)  # x and y both assigned, are they used?

# Chained assignment
m1 = m2 = m3 = 99  # only m2 is used
print(m2)

# Comment mentioning a variable (should not count)
# this talks about variable a

# String mentioning a variable (should not count)
log = "this string mentions variable c"

def nested_function_example():
    outer = 5  # assigned
    def inner_function():
        inner = outer + 1
        inner_unused = 2  # unused inside inner_function
        return inner
    return outer
