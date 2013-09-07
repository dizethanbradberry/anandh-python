# Program to find all duplicates in a list

def dups(l):
 s=[]
 for i in range(len(l)):
  if l[i] in l[i+1:] and l[i] not in s:
   s.append(l[i])
 return s
print 'Testing phase--Use integer list' 
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(int(raw_input("Enter the element %d:" % i)))
print 'Original list=',l
print 'dups(',l,')=',dups(l)
