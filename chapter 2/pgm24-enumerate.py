# Program to implement enumerte function

def enumerate(a):
 return [(i,a[i]) for i in range(len(a))]
print enumerate([2,'fg','rg',6])
