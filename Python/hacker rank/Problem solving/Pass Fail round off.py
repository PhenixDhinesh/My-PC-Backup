import math
import os
import random
import re
import sys

def gradingStudents(grades):
    
#From here to
    
    l=[]
    for i in grades:
        if i<38:
            l.append(i)
        else:
            if (i+1)%5==0 or (i+2)%5==0:
                if (i+1)%5==0:
                    l.append(i+1)
                else:
                    l.append(i+2)
            else:
                   l.append(i) 
    return l
    
#here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
