n=input("Enter students name:\n")
subjects = ["Math", "Physics", "Chemistry", "PCC", "Mechanics","BEE"]
total=0
grades={}
for subject in subjects:
    marks=float(input(f"Enter marks for {subject}: \n"))
    total+=marks
    if marks in range(80,101):
        print("Grade:O")
    elif marks in range(75,80):
        print("Grade:A")
    elif marks in range(70,75):
        print("Grade:B")
    elif marks in range(60,70):
        print("Grade:C")
    elif marks in range(50,60):
        print("Grade:D")
    elif marks in range(45,50):
        print("Grade:E")
    elif marks in range(40,45):
        print("Grade:P")
    elif marks in range(0,40):
        print("Grade:F")

average=total/len(subjects)
print("\nFinal Report:")
print("Total marks:",total)
print(f"Average marks:{round(average,2)}")
if 80 <= average <= 100:
    print("Final Grade: O")
elif 75 <= average < 80:
    print("Final Grade: A")
elif 70 <= average < 75:
    print("Final Grade: B")
elif 60 <= average < 70:
    print("Final Grade: C")
elif 50 <= average < 60:
    print("Final Grade: D")
elif 45 <= average < 50:
    print("Final Grade: E")
elif 40 <= average < 45:
    print("Final Grade: P")
elif 0 <= average < 40:
    print("Final Grade: F")

max_marks=len(subjects)*100
percentage = (total / max_marks) * 100
print(f"Percentage:{round(percentage,2)}%",)

if average>=40:
 print("Status: Pass")
else:
    print("Status:Fail")





