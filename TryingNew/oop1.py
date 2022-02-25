# Create a class that captures students. 
# Each student has a first name, last name, class year, and major. Create two examples of students.


from mimetypes import init



class Student:
    
    def __init__(self,fName,sName,cYear,mJ,Number) :
        self.firstName=fName
        self.lastName =sName
        self.classYear=cYear
        self.major=mJ
        self.addMissionNo=Number
# no input it is a normal pass to test the class 

student1=Student("Sudip","Dutta",2001,10,500120010123)

#now we will take a input and pass the value 
# to the function,so that it will be modular

# These are the inputs by the user and then 
# these values will be passed as arguments 

FirstNameOfStuent=input("Enter your First Name :")
SecondNameOfStudent=input("Enter your last Name :")
CurrentYear=int(input("Enter your Current Standerd : "))
MajorOfStudent=int(input("Enter your Current Mejor : "))
admissionNumber=int(input("Enter your Addmission Number  : "))

#These values will be the argumrnts to the class 

Student2=Student(FirstNameOfStuent,SecondNameOfStudent,CurrentYear,MajorOfStudent,admissionNumber) 
