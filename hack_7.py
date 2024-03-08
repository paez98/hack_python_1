"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    num = -1
    while num < 5:
        num += 1
        result.append(num)
    result.reverse()
    return result

fn_hack_7()