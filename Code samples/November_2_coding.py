# coding done in November 2, 2020 lecture

# an iterative version of the factorial function
def fact(n):
   prod = 1
   for i in range(n,1, -1):
      prod *= i
   return prod

# a recursive version of the factorial function
def r_fact(n):
    if n == 1:
        return 1
    else:
        return n * r_fact(n-1)

# 5! = 5 * 4!  4! = 4 * 3!
# n! = n * (n-1)!
# an iterative function for generating fibonacci numbers
def fib(n):
    print(n)
    if n <= 3:
        return n
    else:
        fib = [1, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return (fib[n-1])


# a recursive function for generating fibonnaci numbers
def rfib(n):
   if n < 2:
      return 1
   else:
      return (rfib(n-1) + rfib(n-2))

if __name__ == "__main__":

# palindrome code
def r_pal(ispal):
    #ispal is a string that may or may not be a palindrome:
    #first the three base cases
    if len(ispal) == 0 or len(ispal) == 1:
        return True
    elif ispal[0] != ispal[-1]:
        return False
    else:
        return r_pal(ispal[1:-1])