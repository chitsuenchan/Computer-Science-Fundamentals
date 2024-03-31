
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    lcm_a = a[0]
    gcd_b = b[0]

    # Find the LCM of elements in array 'a'
    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])

    # Find the GCD of elements in array 'b'
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])

    count = 0
    multiple = lcm_a
    # Count the multiples of 'lcm_a' that evenly divide 'gcd_b'
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a

    return count

# Sample Input
a = [2, 4]
b = [16, 32, 96]

getTotalX()