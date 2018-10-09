# CTI-110 
# P3HW4 - Roman Numerals
# Palti Kerr
# 7 October 2018
 


# Prompt user to enter a number
UserNumber = int(input('Enter a number'))

# Write an if statement to assign Roman Numeral value for 1
if UserNumber == 1:
    print('The Roman Numeral equivlant is: I')
# Write else if statements to assign Roman Numeral values for 2-10 
elif UserNumber == 2:
    print('The Roman Numeral equivlant is: II')
elif UserNumber == 3:
    print('The Roman Numeral equivlant is: III')
elif UserNumber == 4:
    print('The Roman Numeral equivlant is: IV')
elif UserNumber == 5:
    print('The Roman Numeral equivlant is: V')
elif UserNumber == 6:
    print('The Roman Numeral equivlant is: VI')
elif UserNumber == 7:
    print('The Roman Numeral equivlant is: VII')
elif UserNumber == 8:
    print('The Roman Numeral equivlant is: VIII')
elif UserNumber == 9:
    print('The Roman Numeral equivlant is: IX')
elif UserNumber == 10:
    print('The Roman Numeral equivlant is: X')
# Write else statement for any number that doesn't match 1-10
else:
    print('!Error! Please enter a number between 1-10.')
       





