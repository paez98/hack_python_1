"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    resultado = result.replace(result, "f00z1m@n")
    return resultado