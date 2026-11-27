class Student:
    name = None
    surname = None
    age= None
    grade= None
    def set_data(self,name, surname,age,grade):
        self.name=name
        self.surname=surname
        self.age=age
        self.grade=grade

    def new_grade(self,new_grade):
        self.grade= new_grade
    def get_data(self):
        print( self.name,self.surname,self.age,self.grade)

    
                
                
                




student1= Student()
student1.set_data('Test', 'Case', 45, 50)
student1.new_grade(100)
student1.get_data()