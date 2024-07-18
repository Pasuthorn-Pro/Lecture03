first_score_test = int(input("Enter first test score: "))
second_score_test = int(input("Enter second test score: "))
third_score_test = int(input("Enter third test score: "))

average = ((first_score_test + second_score_test + third_score_test)/3)
print("average is ", format(average,".2f"))

if average >= 95 :
    print("Congratulations\nThat's a great average!")