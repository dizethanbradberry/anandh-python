# Program to sort a list of strings based on extensions

def extsort(l):
  return sorted(l,key=lambda x: x.split('.')[1])
 

n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(raw_input("Enter the string %d:" % i))
print 'Original list=',l
print 'extsort(',l,')=',extsort(l)
