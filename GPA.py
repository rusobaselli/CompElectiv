subj1 = raw_input ("Enter your subject?")
subj2 = raw_input ("Enter your subject?")
subj3 = raw_input ("Enter your subject?")
subj4 = raw_input ("Enter your subject?")

print "1. ", subj1 
grade1 = raw_input("Enter your grade ")
print "2. ", subj2
grade2 = raw_input("Enter your grade")
print "3. ", subj3
grade3 = raw_input("Enter your grade")
print "4.", subj4
grade4= raw_input ("Enter your grade")


if grade1 == "A":
    grade1 = 4.00
elif grade1 == "B": 
    grade1 = 3.00
elif grade1== "C": 
    grade1= 2.00
elif grade1 == "D":
    grade1= 1.00
elif grade1== "F":
    grade1 =0.00
print grade1 


if grade2 == "A":
    grade2 = 4.00
elif grade2 == "B": 
    grade2 = 3.00
elif grade2== "C": 
    grade2= 2.00
elif grade2 == "D":
    grade2= 1.00
elif grade2== "F":
    grade2 =0.00
print grade2
