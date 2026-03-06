class Person:

    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    # 讓 stu.age 可以讀取 self._age
    @property
    def age(self):
        return self._age
    
    # 讓 stu.age = value 時，實際修改 self._age
    @age.setter
    def age(self,age):
        self._age=age
    
    def play(self):
        print(f"{self._name}正在愉快地玩耍")

    def watch_movie(self):
        if self._age>=18:
            print(f"{self._name}能觀看所有電影")
        else:
            print(f"{self._name}只能觀看普通電影")
    

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade=grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        self._grade=grade
    
    def study(self,course):
        print(f"{self._grade}的{self._name}正在學習{course}")

class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title=title
    
    @property
    def title(self):
        return self._title
    
    @title.setter()
    def title(self,title):
        self._title=title

    def teach(self,course):
        print(f"{self._name}正在講{course}課")




def main():
    stu=Student("Andy",15,"國三")
    stu.study("數學")
    stu.watch_movie()

    t=Teacher("Alan",38,"程式設計")
    t.teach("Python 程式設計")
    t.watch_movie()