a,b,c = map(int, input().split())


def divideEnque(base,exponent,division):

    if exponent == 1:
        return base % division

    elif exponent%2 == 0:
        halfResult = divideEnque(base,exponent//2,division)
        return (halfResult * halfResult) % division
        
    elif exponent%2 == 1:
        return (base * divideEnque(base, exponent-1, division)) % division


print(divideEnque(a,b,c))