from email.policy import default
from os import makedirs
import random 
import json

from classes import Student , GradeManager 
from jsonFile_handler import save_as_json,load_from_json


   
stud=load_from_json()
data_arr=[]
for i in stud:
     data_arr.append(stud[i])


markmanager=[]
for i in data_arr:
     student=Student(i['name'],i['subjects'],i["id"])
     markmanager.append(student)

grademanager=GradeManager(markmanager)




while(True):
     print("""\n
     1.Display Report(marks and grade of all students \n 
     2.Add new Student  \n 
     3.Update student Records \n 
     4.delete a student Record \n 
     5.Exit \n""")

     ch=int(input("enter your choice (1 - 5): "))
     if ch==1:
          grademanager.view_Report()
          continue
     elif ch==2 :
          name=input("enter student name : ")
          math,english,science=input("Enter the subject marks (Math,English,Science):").split(",")
          subjects={"math":int(math),"english":int(english),"science":int(science)}
          id=f"{random.randint(1,1000)}-{name[0].upper()}"
          status=grademanager.add_student(name,subjects,id)
          print(status)
          continue 
     elif ch==3:
          while(True):
               try: 
                    id=input("Enter the student ID")
                    subject ,score =input("enter the subject and score to be updated (subject,score): ").split(",")
                    status=grademanager.update_student_score(id,subject, int(score))
                    print(status)
                    break
               except Exception as e : 
                    print("Enter valid data!! ")
                    continue
          continue
     elif ch==4:
          while(True):
               try:
                    id=input("Enter the student ID : ")
                    status=grademanager.delete_student(id)
                    print(status)
                    break
               except Exception as e :
                    print("Enter Valid Data!!")
                    continue 
     elif ch==5:
          grademanager.create_json()
          break

     else:
          print("!!  Enter a Valid Option  !!")