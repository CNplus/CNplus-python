def 打印(a,b):
    str(b)
    if a==1:
        print(b)
    elif a == 2:
        print(b,end=' ')

def 判断(a,b,c):
    if b == '==':
        if a == c:
            return 'true'
        else:
            return 'false'
    elif b == '!=':
        if a != c:
            return 'true'
        else:
            return 'false'
    elif b == '<':
        if a < c:
            return 'true'
        else:
            return 'false'
    elif b == '<=':
        if a <= c:
            return 'true'
        else:
            return 'false'
    elif b == '>':
        if a > c:
            return 'true'
        else:
            return 'false'
    elif b == '>=':
        if a >= c:
            return 'true'
        else:
            return 'false'
    
def 随机数(a,b):
    return random.randint(a,b)
