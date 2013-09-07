# Program to implement parse_csv function to parse .csv files
import sys
def parse_csv(filename):
 return [x[:-1].split(',') for x in open(filename,'r').readlines()]
filename=sys.argv[1]
print 'parse_csv(',filename,')=',parse_csv(filename)
 
