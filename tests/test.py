# Global assignments
a = 5  # unused
b = 10 # used later
c = "test"  # unused
d = 20  # used in function
e = 50  # unused
f = 1234  # unused
g = 4321  # used in function but in a tricky way

def foo(x, y, z):
    x = 100  # reassigned, but used later
    m = 200  # unused
    n = x + y
    o = 0  # unused
    w = 1  # unused
    return n + z

def bar():
    p = 1  # unused
    q = 2  # used inside loop
    for i in range(5):
        print(q)

    r = 3  # unused
    s = "hello"  # unused
    t = s + " world"  # used
    unused_inside_if = 99  # assigned inside if but unused
    if False:
        zzz = 123  # unreachable assignment
        unused_inside_if = 100

def baz():
    temp = 123
    temp2 = 456  # unused
    print("temp is", temp)
    print(d)  # uses global d

def unused_function_one():
    ghost_var = 111  # unused
    return  # never called

def unused_function_two(a, b):
    unused_in_function = a + b  # unused
    return 0  # never called

# Tuple unpacking (could break basic analyzers)
x, y = (1, 2)  # x and y both assigned, only y used
print(y)

# Chained assignment
m1 = m2 = m3 = 99  # only m2 is used
print(m2)

# Comment mentioning a variable (should not count)
# this talks about variable a

# String mentioning a variable (should not count)
log = "this string mentions variable c"

def nested_function_example():
    outer = 5  # assigned and used
    def inner_function():
        inner = outer + 1
        inner_unused = 2  # unused inside inner_function
        return inner
    return outer

def function_using_g():
    result = g * 2  # uses global g
    return result

def complex_unused():
    for i in range(10):
        if i > 100:
            impossible_unused = 999  # unreachable practically
    z = 5  # unused

def tricky_function(x):
    if x:
        a1 = 1  # assigned if x true
    else:
        a2 = 2  # assigned if x false
    # Neither a1 nor a2 used later
    return x
