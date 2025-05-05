def func_with_return():
    print("start")
    return
    print("this is unreachable")  # should be flagged

def func_with_if():
    if True:
        print("in if")
        return
        print("dead in if")       # should be flagged
    else:
        print("in else")
        return
        print("dead in else")     # should be flagged

def func_with_loop():
    for i in range(3):
        break
        print("never reached")    # should be flagged
    else:
        print("else block")       # reachable

def func_with_raise():
    raise Exception("oops")
    print("after raise")          # should be flagged

def func_with_continue():
    for i in range(2):
        continue
        print("after continue")   # should be flagged
