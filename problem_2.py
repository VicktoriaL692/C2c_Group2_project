#File 2 (problem2.py): Write a function to calculate the factorial of a number.

#Example:
#Input: 5
#Output: 120

def factorial(n):
   if n == 0: 
      return 1
   else: 
      return n * factorial(n - 1)

print(factorial(5)) 
