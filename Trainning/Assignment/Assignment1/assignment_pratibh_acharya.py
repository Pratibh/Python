#!/usr/bin/python


# Dictionary containing student information. 
student_information = {'Name': 'Pratibh Acharya', 'Address': 'Dhapasi', 'Age':'23', 'University':'TU', 'Course':'BSC CSIT', 'Semester':'','College':'DWIT'};

#Storing all the semesters in a list.  
semester1_percentage =[80,89,50];
semester2_percentage =[90,84,52];	
semester3_percentage =[90,65,76];
semester4_percentage =[70,99,55];
semester5_percentage =[80,82,66];
semester6_percentage =[40,41,40];
semester7_percentage =[80,15,60];
semester8_percentage =[67,80,50];

semester_information ={'Semester 1':'semester1_percentage' , 'Semester 2':'semester2_percentage', 'Semester 3':'semester3_percentage', 'Semester 4':'semester4_percentage', 'Semester 5':'semester5_percentage', 'Semester 6':'semester6_percentage', 'Semester 7':'semester7_percentage', 'Semester 8':'semester8_percentage'};

#Adding the list information to the key:'Semester' defined in dictionary:student_information 
student_information['Semester'] = semester_information;


print "++++++++++++++++++++++++++++++++++++++++++++++++"
print "Student Information"
print "++++++++++++++++++++++++++++++++++++++++++++++++	"
print "Name:", student_information['Name']
print "Address:", student_information['Address']
print "Age:", student_information['Age']
print "University:", student_information['University']
print "Course:", student_information['Course']
print "Semester:", student_information['Semester']
print "College:", student_information['College']


print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print semester_information['Semester 1']
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	



