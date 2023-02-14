#condition controlled loops
#sufiyah sajan
#Part A

print("Triangle Validity - only enter positive numbers or zero")
print()
triangle = 'yes'
while triangle == 'yes':
    point1x = input("Enter the X position of point 1: ")
    while float(point1x) < 0:
        point1x = input("please enter a non-negative number: ")
    point1y = input("Enter the Y position of point 1: ")
    while float(point1y) < 0:
        point1y = input("please enter a non-negative number: ")
    print()
    point2x = input("Enter the X position of point 2: ")
    while float(point2x) < 0:
        point2x = input("please enter a non-negative number: ")
    point2y = input("Enter the Y position of point 2: ")
    while float(point2y) < 0:
        point2y = input("please enter a non-negative number: ")
    print()
    point3x = input("Enter the X position of point 3: ")
    while float(point3x) < 0:
        point3x = input("please enter a non-negative number: ")
    point3y = input("Enter the Y position of point 3: ")
    while float(point3y) < 0:
        point3y = input("please enter a non-negative number: ")
    print()
    print("Here are the lengths of each side of the triangle:")
    side1 = ((((float(point1x) - float(point2x))**2) + ((float(point1y) - float(point2y))**2))**0.5)
    firstside = format(float(side1), '.2f')
    print("Side 1: ", firstside)
    side2 = ((((float(point1x) - float(point3x))**2) + ((float(point1y) - float(point3y))**2))**0.5)
    secondside = format(float(side2), '.2f')
    print("Side 2: ", secondside)
    side3 = ((((float(point3x) - float(point2x))**2) + ((float(point3y) - float(point2y))**2))**0.5)
    thirdside = format(float(side3), '.2f')
    print("Side 3: ", thirdside)
    print()
    s1 = round(side1, 2)
    s2 = round(side2, 2)
    s3 = round(side3, 2)
    if (s1+s2) > s3 and (s2+s3) > s1 and (s3+s1) > s2:
        print("the triangle is valid")
        if s1 == s2 == s3:
            print("the triangle is equilateral")
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print("the triangle is isosceles")
        else:
            print("the triangle is scalene")
    else:
        print("the triangle is not valid")
    triangle = input("Would you like to test another triangle? (yes/no): ")

