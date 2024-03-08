"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    num = -1
    while len(result) < 6:
        num += 2
        result.insert(num,'@')
        
    return result

fn_hack_9()