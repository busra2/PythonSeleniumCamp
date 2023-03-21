# add one student
def  addStudents():
     
     nm1 = input("Enter Name ")
     srnm1 = input("Enter Surname")
     list.append(nm1 + srnm1)
     print(nm1 + srnm1, "Successfully added!!")

# add one student
def deleteStudents():
    nm1 = input(" Enter Name ")
    srnm1 = input(" Enter Surname")
    list.remove(nm1+srnm1)
    print(nm1 + srnm1 ,"deleted ")

# add multiple students
def multipleAddStudents():
    num=int(input("How Many Student Will You Add?"))
    count=0
    while count<num:
         nm1 = input(" Enter Name ")
         srnm1 = input(" Enter Surname")
         list.append(nm1+srnm1)
         print(nm1 + srnm1 ,"added ")
         count+=1
# delete multiple students
def multipleDeleteStudents():
    num=int(input(" How Many Student Will You Add"))
    count=0
    while count<num:
         nm1 = input("  Enter Name")
         srnm1 = input("Enter Surname ")
         list.remove(nm1+srnm1)
         print(nm1 + srnm1 ,"deleted ")
         count+=1
# find  student number [index number in the list is student number ]
def findStudentNumber():
    nm1 = input(" Enter Name")
    srnm1 = input("Enter Surname")
    if nm1 + srnm1 in list:
        num = list.index(nm1 + srnm1)
        print(str(nm1 + srnm1) , "student's number is: " , str(num))
    else:
         print("Try again !")
#viewing student 
def printStudent():
        for i in list:
            print(i)

list=[] # holds student list 
 
 #main step 
print(""" 
1. Add Student
2. Delete Student
3. Add Multiple Student 
4. Delete Multiple Student 
5. Find Student Number
6. Print Student list
7. Exit
""")
      
while True:
    islem = int(input("Please Select Steps: "))

    if islem == 1:
        addStudents()

    elif islem == 2:
        deleteStudents()

    elif islem == 3:
        multipleAddStudents()

    elif islem == 4:
        multipleDeleteStudents()

    elif islem == 5:
        findStudentNumber()

    elif islem == 6 :
        printStudent()

    elif islem ==  7 :
        print("Exit Successful...")
        break

    

   