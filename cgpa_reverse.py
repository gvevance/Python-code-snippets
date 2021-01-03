# calculate gpa to get required cgpa

current_cgpa = 7.71
credits_completed = 283

print("This program can calculate GPA required to get CGPA  . \n")
print("You have completed 283 credits with a CGPA of 7.71. You have 268 credits remaining.\n")

dream_cgpa = float(input("Enter CGPA required : "))
available_creds = int(input("In how many credits : "))

gpa_req = (dream_cgpa*(credits_completed + available_creds) - (current_cgpa * credits_completed)) / available_creds

if gpa_req > 10 or gpa_req < 5 :
    print("Not possible . Exiting ...")
    quit()

print(f"GPA required = {gpa_req}")