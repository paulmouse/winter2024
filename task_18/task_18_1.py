class Task:  # темы обучения
    def __init__(self, taskList):
        self.taskList = taskList
        # self.taskDone = False # изначально не решена
    # def taskSolution(self):     # метод "решения"
    #     self.taskDone = True
class Teacher:  # преподаватель
    def __init__(self, name):
        self.name = name
        self.work = 0  # учет сколько тем и учеников

    def taskAssignToGroup(self, task):  # передача заданий
        for i in Student.group:  # цикл по списку студентов
            i.takeTask(task)  # вызов метода студента получения заданий
            self.work += 1
    def taskAssignToStudent(self, task, student):  # индивидуальное обучение
        student.takeTask(task)  # вызов метода ученика получения информации
        self.work += 1
    def checkTasks(self, student):
        for task in student.sloved:
        #     if self.taskDone:
            student.checked.append(task)
        #     else:
        #         pass

    def info(self):  # метод печати, что ученик получил, решил, получил ответ
        print(self.name, f'обработал работ: {self.work}')

class Student:  # класс учеников
    group = []  # список учеников

    def __init__(self, name):
        self.received = [] # задания которые студент получил
        self.sloved = []  # задания которые студент решил
        self.checked = []  # задания которые преподаватель принял
        self.name = name
        Student.group.append(self) # студент отправляется в группу
        #print(self.sloved)

    def takeTask(self, task):  # метод получения заданий
        self.received.append(task)

    def make(self): # метод выполнения
        for i in self.received:
            self.sloved.append(i) # добавляем в лист решенных

    def info(self):  # метод печати, что ученик получил, решил, получил ответ
        print(self.name, end=' получил задачи по теме: ')
        # for i in self.received:
        #     print(i, end=', ')
        print(self.received)
        print(end='решил задачи по теме: ')
        # for i in self.sloved:
        #     print(i, end=', ')
        print(self.sloved)
        print(end='получил ответы на задачи по теме: ')
        # for i in self.checked:
        #     print(i, end=', ')
        print(self.checked)
        print('Теперь', self.name, 'знает',len(self.checked), 'тем(ы)')

teacher = Teacher('Михаил')

student1 = Student('Вася')
student2 = Student('Петя')
student3 = Student('Коля')

taskList = Task(['class', 'object', 'inheritance', 'polymorphism', 'encapsulation'])

teacher.taskAssignToGroup(taskList.taskList[1])
teacher.taskAssignToGroup(taskList.taskList[0])
teacher.taskAssignToGroup(taskList.taskList[2])
teacher.taskAssignToGroup(taskList.taskList[3])

teacher.taskAssignToStudent(taskList.taskList[4], student1)

student1.make()

teacher.checkTasks(student1)
teacher.checkTasks(student2)

teacher.info()
print(student1.info())
print(student2.info())
print(student3.info())