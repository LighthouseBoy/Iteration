newnumber = 0
numbertotal = 0
no_of_no = int(input("How many numbers do you want to average?: "))
for counter in range (no_of_no):
    newnumber = int(input("pick a number: "))
    numbertotal = numbertotal + newnumber
average = numbertotal / no_of_no
print(average)
