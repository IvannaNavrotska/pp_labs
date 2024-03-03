def gcd (a,b):
    if a == 0 and b == 0:
        return
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)


def fibonacci (f):
    if f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)
      