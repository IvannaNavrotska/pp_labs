answer = input("gcd or fibonacci? put 'gcd' or 'fib': ")

if answer == 'gcd':

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

else:

    f = int(input('give me num of fibonacci you wanna know: '))

    def fibonacci (f):
        if f == 0 or f == 1:
            return 1
        else:
            return fibonacci(f-1) + fibonacci(f-2)
    
    print(f'here is your fibonacci: {fibonacci(f)}')  