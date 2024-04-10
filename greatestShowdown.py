largest = False
n1 = int(input("Please enter three numbers: "))
n2 = int(input(""))
n3 = int(input(""))

if n1 > n2 and n1 > n3 and largest == False:
    print("The largest number is: " ,n1)

elif n2 > n1 and n2 > n3 and largest == False:
    print("The largest number is: " ,n2)

elif n3 > n1 and n3 > n1 and largest == False:
    print("The largest number is: " ,n3)

if n1 < n2 and n1 < n3:
        print("1The smallest number is: " ,n1)
elif n2 < n1 and n2 < n3:
        print("2The smallest number is: " ,n2)
elif n3 < n1 and n3 < n2:
        print("3The smallest number is: " ,n3)