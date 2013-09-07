# Program to find factorial of a number by using function product
def product(l):
 p=1
 for i in l:
  p=p*i
 return p
def factorial(n):
 return product(range(1,int(x)+1))
print '_____Factorial_____'
x=raw_input("Enter the number:")
print 'factorial=',factorial(x)
