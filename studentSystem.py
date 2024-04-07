
def getNumberInput(prompt:str):
    while True: 
        try:
            number=int(input(prompt,))
            if number>0:
                return number
            break
        except ValueError:
            print('Please enter a integer greater than 1!')


def addStudentInfo():
    studentInfo={}
    studentInfo['name']=input('Enter student name: ')
    studentInfo['email']=input('Enter student email: ')
    studentInfo['age']=getNumberInput('Enter student age: ')
    return studentInfo

def addCourseInfo(studentInfo:dict):
    #arrow student has mutiple courses
    if 'course' not in studentInfo:
        studentCourse=[]
    else:
        studentCourse=studentInfo['course']    
    studentCourse.append(input('Enter course name: '))
    studentCourse.append(getNumberInput('Enter course grade(0-100): '))
    studentInfo['course']=studentCourse
    return studentInfo

def showStudentInfo(studentList:list):
    print(f"There are {len(studentList)} students in the class!")
   
    for info in studentList:
        print('------------------------------------')
        if 'course' in info:
            print("The following student have taken courses and their grades:")
            print(f"Name: {info['name']}")
            for i in info['course']:
                print(i)       
        else:
            print('The student do not take any course and his information are:')
            print('Name:',info['name'])
            print('Email:',info['email'])
            print('Age:',info['age'])
        print('------------------------------------')    

def studentSystem():
    studentList=[] #list of student information
    studentNum=getNumberInput('How many students in the class: ') #ask for the number of students 
    if studentNum >=1:
        for i in range(studentNum):
            studentInfo = addStudentInfo()
            studentList.append(studentInfo)
   
    while True:
        addCourse=input('Do you want to add a course for the student? (yes/no): ')
        if addCourse=='yes':
            studentName=input('Enter the name of the student you want to add a course for: ')
            ifFound=False
            for info in studentList:
                if info['name']==studentName:
                    addCourseInfo(info)
                    ifFound=True
                    break
            if ifFound==False:
                print('Student not found!')    
              
        elif addCourse=='no':
            showStudentInfo(studentList)
            break       


studentSystem()        