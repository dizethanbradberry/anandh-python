# Program to implement cumulative sum in list
def cumulative_sum(l):
 a=[]
 sum=0
 for item in l:
  sum=sum+item
  a.append(sum)
 return a
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(int((raw_input("Enter the element %d:" % i))))
print 'Original list=',l
print 'cumulative_sum(',l,')=',cumulative_sum(l)
