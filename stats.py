#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

#Worked with Kevin on this code
import sys
import math

#1. Make sure list is no longer in text
p = []
sum = 0
sigsq = 0

for i in sys.argv[1:]:
    p.append(float(i))
#print(p) no longer in text

#2.Count the variables in list
count = 0
for i in range(len(p)):
    count += p[i]
print('Count:', len(p))
#3.Find min and max
p.sort()
print('Minimum:', p[0]) #Minimum
print('Maximum:', p[-1]) #Maximum
#5. Find mean
for j in range(len(p)):
    sum = sum + p[j]
mean = sum/len(p)
print('Mean:', f'{mean:.3f}')
#find Std. dev
for k in range(len(p)):
    sigsq = sigsq + (p[k]- mean) ** 2
before = sigsq / len(p)
print('Std. Dev:', f'{math.sqrt(before):.3f}')
#Find median
med_def = len(p) // 2
med_even = 0
if len(p) % 2 == 1: print('Median', f'{p[med_def]:.3f}')
if len(p) % 2 == 0:
        med_even = (p[med_def-1]+p[med_def])/2
        print('Median:', med_even)

"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
