"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    resultado = result.replace(result, "f,0,0,z,1,m,@,n").upper()
    resultado = resultado.split(",")
    print(resultado)
    return resultado

fn_hack_10()