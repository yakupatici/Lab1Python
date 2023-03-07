print("Welcome to the grade calculation")

name = input("Enter your name : ")
lab = int(input("Enter your lab grade :"))
midterm = int(input("Enter your midterm grade : "))
final = int(input("Enter your final grade : "))
lastScore = float(lab * 0.25) + float(midterm*0.35) + float(final *0.40)


print("Name : " , name)
print("Lab  : " ,lab)
print("Midterm : " , midterm)
print("Final : " , final)
print("Last Score : " , lastScore)
