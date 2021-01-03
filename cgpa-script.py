# take user input and calculate cgpa if things go according to his/her plan

current_cgpa = 7.71
credits_completed = 283

print("This program can calculate your CGPA if things go according to your plan. \n")
print("You have completed 283 credits with a CGPA of 7.71. You have 268 credits remaining.\n")

new_creds = int(input("Enter 'extra' credits you want to calculate CGPA after : "))
if new_creds > 268 :
    print("Invalid credits entered . Exiting ...")
    quit()

gpa = float(input("Enter probable CGPA : "))
new_cgpa = (credits_completed * current_cgpa + new_creds * gpa) / (credits_completed + new_creds)

print(f"Your CGPA will be {new_cgpa}")
