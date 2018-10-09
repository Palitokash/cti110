# CTI-110 
# P3LAB - Debugging Grade Calculator
# Palti Kerr
# 7 October 2018

def main():
    # This program takes a number grade and outputs a letter grade.
    print('This program calculates a letter grade based off of an\
 number input')
    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    
score = int(input('Enter grade: '))

if score >= 90:
    print('Your grade is A')
elif score > 79:
    print('Your grade is B')
elif score > 69:
    print('Your grade is C')
elif score > 59:
    print('Your grade is D')
else:
    print('Your grade is F, study up and re-test.') # TO DO: finish this







# program start
main()
    
