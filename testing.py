def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    if b==0:
        raise ValueError("Can`t divide")
    else:
        return a//b







