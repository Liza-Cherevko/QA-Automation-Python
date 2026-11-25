class Student:
    name=None
    surname = None
    age = None
    average_score=None
    
    def set_student_data(self, name, surname, age, average_score ):
        self.name= name
        self.surname = surname
        self.age=age
        self.average_score=average_score
    def new_average_score(self,new_score):
        self.average_score = new_score
    def get_student_data(self):
       print(
    'Name:', self.name,
    ', Surname:', self.surname,
    ', Age:', self.age,
    ', Average:', self.average_score
)



student1 = Student()
#student1.name = 'Liza'
#student1.age = 26
#student1.average_score = 95

student1.set_student_data('Liza','Cherevko', 26, 95)
student1.new_average_score(100)
student1.get_student_data()
