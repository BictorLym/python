def calc(x, y):
    add(x, y)
    sub(x, y)
    mul(x, y)
    div(x, y)

def add(x,y):
    ans = x + y
    print(f'({x} + {y}) = {ans}')
def sub(x,y):
    ans = x - y
    print(f'({x} - {y}) = {ans}')
def mul(x,y):
    ans = x * y
    print(f'({x} * {y}) = {ans}')
def div(x,y):
    ans = x / y
    print(f'({x} / {y}) = {ans}')

x = 20; y= 10
calc(x,y)
