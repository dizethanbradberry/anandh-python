# Program to find unique elements in a list

def unique(l):
 a=[]
 for i in l:
  if a!='' and i not in a:
   a.append(i)
 return a
print 'Testing phase--Use integer list' 
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(int((raw_input("Enter the element %d:" % i))))
print 'Original list=',l
print 'unique(',l,')=',unique(l)
