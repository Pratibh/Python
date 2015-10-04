from Employee import Employee

__author__ = 'pratibh'

employee=Employee()

def start():

    menu=raw_input("Enter 1 for new employee, 2 to view list, 3 to search employee by name and 4 to exit the application.")
    if(menu=="1"):
        newInput()
    elif(menu=="2"):
        viewList()
    elif(menu=="3"):
        searchByName()
    else:
        print "Thank You For Visiting"
        exit()

# Automatically increasing the Employee Number and returning as input
def getEmployeeNumber():
    fileName="employeeNumber.txt"
    try:
        fp=open(fileName,"r")
        employeeNumber=int(fp.read())
        increasedEmployeeNumber=employeeNumber+1
        fp.close()
        fp=open(fileName,"w")
        fp.write(str(increasedEmployeeNumber))
        fp.close()
        return employeeNumber
    except Exception as  error:
        print "Error!! File "+fileName+" Not found or File is Empty!!"
        getInput()




# Check if input parameter which should be Numeric are right or not.
def checkInput(paramName,paramValue):
    try:
        paramValue=int(paramValue)
        return paramValue
    except Exception as error:
        print paramName+" Should be in number"
        getInput()


def checkDate(paramName,paramValue):
    try:
        dataValue = paramValue.split("/")
        if len(dataValue[0]) == 4 and len(dataValue[1]) <=2 and len(dataValue[1]) >0 and len(dataValue[2]) <= 2 and \
                        len(dataValue[2])>0:
            return paramValue
    except Exception as error:
        print "The Date Format of "+paramName+" is not matched"
        getInput()




#Taking input from the user and passing it to the writeToFile method.
def getInput():
    print "Employee Info:"
    print "-------------------"
    employee.set_name(raw_input("Name:").title())
    employee.set_address(raw_input("Address:").title())
    age=raw_input("Age:")
    age=checkInput("Age",age)
    employee.set_age(age)
    employee.set_EmployeeNumber(getEmployeeNumber())
    employee.set_Department(raw_input("Department:").title())
    dob=raw_input("Date of Birth(yyyy/MM/DD):")
    dob=checkDate("Date of Birth",dob)
    employee.set_Dob(dob)
    joinDate = raw_input("Join Date:")
    joinDate = checkDate("Join Date(yyyy/MM/DD)",joinDate)
    employee.set_JoinDate(joinDate)
    salary=raw_input("Salary:")
    salary=checkInput("Salary",salary)
    employee.set_Salary(salary)
    return employee  # returning the object of Employee Class



#Writing to file
def writeToFile(employee):
    fileName="employee.txt"
    try:
        employeeFile=open(fileName,"a")
        employeeFile.write("Name:"+employee.get_name())
        employeeFile.write(";Address:"+employee.get_address())
        employeeFile.write(";Age:"+str(employee.get_age()))
        employeeFile.write(";EmployeeNumber:"+str(employee.get_EmployeeNumber()))
        employeeFile.write(";Department:"+(employee.get_Department()))
        employeeFile.write(";DOB:"+employee.get_Dob())
        employeeFile.write(";Join Date:"+employee.get_JoinDate())
        employeeFile.write(";Salary:"+str(employee.get_Salary()))
        employeeFile.write("\n")
    except Exception as error:
        print "File "+fileName+" Not Found or File is empty"
        getInput()




#Search By Employee Name
def searchByName():
    employeeName=raw_input("Enter the Employee Name:").title()
    print "\n"
    employeeInfo={}
    employeeInfo=searchFile(employeeName)
    print "Search For"+employeeName+"\n"
    if(len(employeeInfo)>=1):
        print "-----------------------"
        for infoCollection  in employeeInfo.values():
            infoCollection=infoCollection.split(";")
            for info in infoCollection:
                print info
    else:
        print "No ResultFound"

    start()


#Search By Employee Name in File
def searchFile(employeeName):
    fileName="employee.txt"
    try:
        readFile=open("employee.txt","r")
        employeeInfo={}
        lines=readFile.readlines()
        employeeNumber=1
        for line in lines:
            if(line.__contains__("Name:"+employeeName)):
                employeeInfo["Employee "+str(employeeNumber)]=line
                employeeNumber += 1
        return employeeInfo
    except Exception as error:
        print "File "+fileName+" Not Found or File is Empty!!"
        start()




#Getting Input
def newInput():
    nextInput=True # To get the first input from the user
    while nextInput:
        employee=getInput() # Getting the user values set in object
        writeToFile(employee)
        ask=raw_input("Enter Y to Continue and N to Break:")
        if(ask.lower()=="y"):
            continue
        else:
            start()





#Display all the list in file
def viewList():
    fileName="employee.txt"
    try:
        readFile=open("employee.txt","r")
        lines=readFile.readlines()
        if(len(lines)>=1):
            print "\nList of Record:"
            print "---------------------------"
            for line in lines:
                line=line.split(";")
                for eachInfo in line:
                    print eachInfo
            start()
        else:
            print "No Result Found!!"
    except Exception as error:
        print "File "+fileName+" Not Found or File is Empty!"



#start
start()