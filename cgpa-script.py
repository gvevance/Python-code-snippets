# cgpa-script.py
# v2

class course:

    # init method or constructor
    def __init__(self , credits_in=0 , gpa_in=0.0 ):
        self._credits = credits_in
        self._gpa = gpa_in

    # return methods
    def gpa_return(self):
        return (self._gpa)
    
    def credits_return(self):
        return (self._credits)

def print_course_queue(arr):       # array with elements as tuples (credits,gpa)
    print("\nCurrent course queue : ")
    for i in arr:
        print(f"{i[0]}\t{i[1]}")
    print("\n",end='')

def calc_cgpa( arr , cred_0 , cgpa_0 ):
    _num = cred_0 * cgpa_0
    _den = cred_0
    for i in arr:
        _num += i[0]*i[1]
        _den += i[0]
    return(_num/_den)
    
# Driver code
# object instantiation
# dummy = course()
cred_0 = 283
cgpa_0 = 7.71
array_0 = []

print("CGPA CALCULATOR")
print("Current CGPA is 7.71. Credits completed = 283\n")

while (True):
    
    _in1 = int(input("Enter course credits [Enter 0 to stop]: "))
    if _in1 == 0:
        break
    _in2 = float(input("Enter probable GPA : "))
    array_0.append((_in1,_in2))
    print_course_queue(array_0)
print("CGPA = ", calc_cgpa(array_0 , cred_0 , cgpa_0 ))
input("Press Enter ... ")