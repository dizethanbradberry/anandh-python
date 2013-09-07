# Program to implement filter function 

def triplets(n):
 return [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(1,n) if x+y==z]
n=int(raw_input('Enter the number'))
print 'triplets(',n,')=',triplets(n)
