print("Enter the Points of the First Exam that is less than or equal to 100")
firstExamPoints = float(input())
firstExamPercentage = firstExamPoints * 0.6
print("The first exam total percentage is " + str(firstExamPercentage))
print("Enter the Points of the Second Exam that is less than is or equal to 100")
secondExamPoints = float(input())
secondExamPercentage = secondExamPoints * 0.4
print("The second exam total percentage is " + str(secondExamPercentage))
totalExamPercentage = firstExamPercentage + secondExamPercentage
print("The total percentage for both exams is " + str(totalExamPercentage))
