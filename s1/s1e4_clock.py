#
# lesson 1 task 4
# electronic clock
# modified!
#

n = int(input())

days = n//(24*60)
hours = n//60 - 24*days
mins = n%60

if mins < 10:
    mins = '0' + str(mins)
    
print('day: '+str(days)+' time: '+str(hours)+':'+str(mins))
