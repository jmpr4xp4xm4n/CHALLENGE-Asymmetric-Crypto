# Euler's totient function:
#
# phi(n) is the number of integers between 1 and n (inclusive)
# that are coprime to n.
#
# The (possible) prime factors of n are given in the second argument.

def phi(n, primes):
    ans = n
    for p in primes:
  if n % p == 0:
    ans = ans*(p-1)/p
    return ans

# Calculate the power tower x^x^x^...^x mod m, where x occurs n times.
# The argument primes must contain all possible prime factors of
# m, phi(m), phi(phi(m)), etc. If m is a power of 10, then [2,5] suffices.

def powertower(x, n, m, primes):
    if n == 1:
  return x % m
    y  = powertower(x, n-1, phi(m, primes), primes)
    return pow(x, y, m)

# Compute 7^7^7^7^7^7^7^7^7^7^7 mod 10**40

print powertower(7, 11, 10**40, [2,5]) 
