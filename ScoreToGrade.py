## Ebtesam Aloubid - 101260655
print("To calculate your over all garde please enter your overall grade received for:")
print (" Note that the full marke is assignet between ()")
# variables that store the user input 
tutorials = int(input("Tutorials (10%)"))
quizzes = int (input("Quizzes (30%)"))
assignments = int (input("Assignment (40%)"))
final = int (input("Final(20%)"))
# calculation to get the result 
result = tutorials + quizzes + assignments + final 
# taking the numerical grade and coverted a letter grade
if result >= 90 :
    print ("Your final grade is A+")
if (result >= 85) and (result< 90) :
    print ("Your final grade is A") 
if (result >= 80) and (result < 85) :
    print ("Your final grade is A-") 
if (result >= 77) and (result < 85) :
    print ("Your final grade is A-") 
if  (result >= 77) and (result< 80) :
    print ("Your final grade is B+") 
if  (result >= 73) and (result< 77) :
    print ("Your final grade is B") 
if  (result >= 70) and (result< 73) :
    print ("Your final grade is B-") 
if  (result >= 67) and (result< 70) :
    print ("Your final grade is C+")
if  (result >= 63) and (result< 67) :
    print ("Your final grade is C") 
if  (result >= 60) and (result< 63) :
    print ("Your final grade is C-")   
if  (result >= 57) and (result< 60) :
    print ("Your final grade is D+")  
if  (result >= 53) and (result< 57) :
    print ("Your final grade is D")  
if  (result >= 50) and (result< 53):
    print ("Your final grade is D-")  
if  result< 50 :
    print ("Your final grade is F") 
else:
    print ("Please enter a valid values") 





