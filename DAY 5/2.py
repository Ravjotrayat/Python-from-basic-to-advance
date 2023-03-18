class Student:
    def __init__(self):
        self.__sid=None
        self.__marks=None
        self.__age=None
        self.__course_id=None
        self.__amount=None

    def set_values(self,sid,marks,age,course_id):
        self.__sid=sid
        self.__marks=marks
        self.__age=age
        self.__course_id=course_id
           
        
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
        
    def validate_age(self):
        if self.__age>=20:
            return True
        else:
            return False

    

    def check_qualification(self):    #if we call one() inside another
                                    # () we have to use self.
        a=self.validate_marks()
        b=self.validate_age()
        if a==b:
            if self.__marks>=65:
                print("Eligible for Admission")
                c=self.course_discount()
            else:
                print("Not Eligible for Admission")
                
        else:
            print("Not Eligible for Admission")

    def course_discount(self):
        if self.__course_id == 1001:
            if self.__marks>=85:
                self.__amount=0.75*25575
                print("Eligible for discount on your course,u have to pay=",self.__amount)
            else:
                 self.__amount=25575

        elif self.__course_id==1002:
            if self.__marks>=85:
                self.__amount=0.75*15500
                print("Eligible for discount on your course,u have to pay=",self.__amount)
            else :
                self.__amount=15500
        else:
            self.__amount="Error in Entering the course...."
        return self.__amount
       

    def get_values(self):
        return self.__amount

s1=Student()
s1.set_values(1,50,22,1002)
s1.check_qualification()
print("Course Fees :",s1.get_values())



                
            
            
        
