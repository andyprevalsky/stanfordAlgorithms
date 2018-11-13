x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def multiply(x, y):
    if x < 10 or y < 10:
        return x * y
    xMid = max(len(str(x)), len(str(y)))//2

    a = x // (10**xMid)
    b = x % (10**xMid)
    c = y // (10**xMid)
    d = y % (10**xMid)
    
    ac = multiply(a, c)
    bd = multiply(b, d)
    ab_cd = multiply((a+b), (c+d))
    ad_bc = ab_cd - ac - bd
    
    res = (10**(xMid*2) * ac) + (10**xMid * ad_bc) + bd
    
    return res

val = [x, y]
print(multiply(val[0], val[1]), multiply(val[0], val[1]) == int(val[0]) * int(val[1]))
