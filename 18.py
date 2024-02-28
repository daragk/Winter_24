import random
from time import sleep

class Teacher:
    def __init__(self, name):
        self.name = name
        self.done_lessons = 0
    def info(self):
        print(f'Учитель {self.name} со стажем работы {self.done_lessons} уроков')
    def give_task(self, student, topic):
        self.done_lessons += 1
        print(f"{self.name} has given homework to {student.name} to do {topic}")
        student.take_task(topic)
    def check_task(self, student):
        print('Идет проверка задания ...')
        sleep(1) #создание интриги :)
        if student.do_and_send_task() == 1:
            print("ура отлично супер")
            student.right_tasks += 1
        else:
            print('задание решено неверно, попробуй еще раз')
            student.wrong_tasks += 1

class Student:
    def __init__(self, name):
        self.name = name
        self.right_tasks = 0
        self.wrong_tasks = 0
    def info(self):
        print(f'Ученик {self.name}, решенных заданий {self.right_tasks}, нерешенных заданий {self.wrong_tasks}')
    def take_task(self, topic):
        print(f'{self.name} усердно работает над заданием {topic}')
    def do_and_send_task(self):
        reshenie = [0, 1]
        return random.choice(reshenie)

class Tasks:
    def __init__(self, topic):
        self.topic = topic #список тем


topics_for_studying = Tasks(['Циклы', 'Объекты', 'Переменные', 'ПП', 'ООП', 'Классы'])

olga_lvovna = Teacher('Olga Lvovna')
petr = Student('Петя')
oleg = Student('Олег')

olga_lvovna.give_task(petr, topics_for_studying.topic[3])
petr.do_and_send_task()
olga_lvovna.check_task(petr)

#olga_lvovna.give_task(oleg, random.choice(topics_for_studying.topic))
#oleg.do_and_send_task()
#olga_lvovna.check_task(oleg)

print()
olga_lvovna.info()
petr.info()
oleg.info()
