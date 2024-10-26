class Student:
    # state 부분 (클래스 변수 선언)
    def __init__(self, name, student_number, classes = None):
        self.name = name # self.__변수이름은, 밖에서 함부로 변수를 바꿀 수 없는 프라이빗 변수이다.
        self.student_number = student_number
        if classes is None:
            self.classes = {}
        else:
            self.classes = classes # self.변수이름으로 바꾼 변수들은 class 내부에선(메서드들 사이에서) 객체마다 호환이 되는 변수이다.
            
    # method 부분 (클래스 함수 선언)
    def get_name(self):
        return self.name
    
    def get_student_number(self):
        return self.student_number 
    
    def get_classes(self):
        return self.classes
    
    def add_classes(self, class_name, credits):
        self.classes[class_name] = credits
        
    def __num_credits(self):
        num_credits = 0
        for c in self.classes.values():
            num_credits += c
        return num_credits
    
    def calc_standing(self):
        N = self.__num_credits() # 리턴값을 받아줄 변수 필요. 내부 메서드를 부를때도, self.을 붙여줘야한다.
        if N < 45:
            return "freshman"
        elif 45 < N < 90:
            return "sophomore"
        elif 90 < N < 135:
            return "junior"
        else:
            return "senior"
        
        
s1 = Student("오세현", "20243064", {"파이썬" : 3, "컴개론" : 3}) # 객체를 만들고, (s1변수는 정보가 엄청 많은 변수이자 객체이다.)
s2 = Student("오민성", "20243063", {"파이썬" : 3, "컴개론" : 3}) 
print(s1.get_name()) # 객체.메서드를 사용한다.
print(s1.name) # 클래스 변수를 부르때도, 객체.변수를 사용한다.(state)


class University_base:
    def __init__(self, name, students = None):
        self.name = name
        if students is None:
            self.students = {students}
        else:
            self.students = students
            
    def get_name(self):
        return self.name
    

class University(University_base):
    def __init__(self, name, students=None): # 상속받는 경우,,state를 써줘여한다.
        University_base.__init__(self, name, students)
        
    def is_enrolled(self, student_number):
        if student_number in self.students.keys():
            return True
        else:
            return False
        
    def enroll_student(self, student):
        if self.is_enrolled(student.get_student_number()): # 함수인자로 객체 그자체를 인자로 받는 경우,, ex) s1.get_student_number == 20243064,,, 리턴값이 바로 나온다.
            return False
        else:
            return True
        
    def num_class_standing(self, class_standing):
        count = 0
        for i in self.students:
            self.students[i].calc_standing() == class_standing
            count += 1
        return count

u1 = University("숭실대", {"20243064" : s1, "20243063" : s2}) # s1, s2는 정보가 굉장히 많은 변수이자 객체이다.
print(u1.num_class_standing("freshman"))