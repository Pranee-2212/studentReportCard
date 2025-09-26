import random 
import json    
from jsonFile_handler import save_as_json,load_from_json


def create_student_dict(student):
          grade=student.get_grade()
          avg=student.calculate_average()
          student_log={
                    "id":student.id,
                    "name":student.name,
                    "subjects":student.subjects,
                    "grade":grade,
                    "average":avg 
               }
          return student_log


class Student:
      
     def __init__(self, name,subjects,id):
          self.name= name
          self.subjects=subjects
          self.id=id
          

     def get_marks(self):
          result=""
          for i in self.subjects:
               result+=i + ":"+ str(self.subjects[i]) + "\n"     
          return result 

     def add_Subject(self,sub_name, sub_score):
               self.subjects[sub_name]=sub_score
               return "successfully added"
     
     def calculate_average(self):
          total=0
          for i in self.subjects:
               total+=self.subjects[i]
          return round(total/len(self.subjects),2)
     
     def get_grade(self):
          average=self.calculate_average()
          if average>=90:
               self.grade="A"
               return "A"
          elif average>=80:
               self.grade="B"
               return "B"
          elif average>=70:
               self.grade="C"
               return "C"
          else:
               self.grade="F"
               return "F"

class GradeManager:
     def __init__(self,students):
          self.students=students

     def add_student(self,name,subjects,id):
          try:
               self.students.append(Student(name,subjects,id))
               self.create_json()
               return "successfully added"

          except Exception as e :
               print("error in adding student")

     def get_student_by_id(self,id):
          for student in self.students:
               if student.id==id:
                    return student
     def view_Report(self):
          for student in self.students:
               student_report=f"{student.name}, id:{student.id} \n {student.get_marks()} \naverage: {student.calculate_average()} \ngrade: {student.get_grade()}"
               print()

               print(student_report)
               print()
          
     def update_student_score(self,id,subject,score):
          student=self.get_student_by_id(id)
          student.add_Subject(subject,score)
          
          return "successfully updated"

     def delete_student(self,id):
          student=self.get_student_by_id(id)
          self.students.remove(student)
          
          return "successfully deleted"

     def create_json(self):
          students_detail=[]
          for student in self.students:
               student_log=create_student_dict(student)
               students_detail.append(student_log)
          
          ids=range(0,len(students_detail))
          json_save={}
          for i in ids:
               json_save[str(i)]=students_detail[i]
          save_as_json(json_save)

     def get_students_list(self):
          return self.students
  