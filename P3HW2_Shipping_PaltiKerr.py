# CTI-110 
# P3HW2 - Shipping Charges
# Palti Kerr
# 7 October 2018
 


# Prompt user to enter the weight of a package
PackageWeight = int(input('Enter the weight of the package in lbs.'))

# Write an if statement to assign rate for packages 2lbs or less
if PackageWeight <= 2:
    print('For a package weighing ' +str(PackageWeight) +' lbs., \
Shipping cost is $1.50')
# Write an else if statement to assign rate for packages 2 - 6lbs 
elif PackageWeight < 7:
    print('For a package weighing ' +str(PackageWeight) +' lbs., \
Shipping cost is $3.00')
# Write an else if statement to assign rate for packages 6 - 10lbs
elif PackageWeight < 11:
    print('For a package weighing ' +str(PackageWeight) +' lbs., \
Shipping cost is $4.00')
# Write an else statement to assign rate for packages 6 - 10lbs
else:
    print('For any package weighing over ' +str(PackageWeight)\
+ ' lbs., Shipping cost is $4.75')
       





