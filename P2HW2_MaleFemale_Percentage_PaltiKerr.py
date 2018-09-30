# Male Female Precentage Calculator 
# 24 Sept 2018
# CTI-110 P2HW2 - Male Female Percentage
# Palti Kerr

# Get the total number of Males in class.
total_Males = int(input('Enter the number of Males in class: '))

# Get the total number of Females in class
total_Females = int(input('Enter the number of Females in class: '))

# Get the total number of students in class.
total_Students = total_Males + total_Females 

# claculate the percentage of males in class.
percentMales = (total_Males / total_Students) 

# Calculate the percentage of females in class.
percentFemales = (total_Females / total_Students) 

#Display the percentage of male and female students.
print (' There are: ' + str(total_Students) + ' students in the class: '\
       +format(percentMales, '.0%') + ' of them are males, ' + \
       format(percentFemales, '.0%') + ' of them are females.' )       





