a = int(input('give me any integer: '))
b = int(input('i need one more to find gcd: '))

def gcd (a,b):
    if a == 0 and b == 0:
        return
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

print(f'here is gcd of those integers: {gcd(a,b)}')