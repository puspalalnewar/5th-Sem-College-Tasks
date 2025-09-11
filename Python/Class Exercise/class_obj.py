class Grandfather : 
    def skill(slef) :
        print("I like to play Football!!")
class Father:
    def skill(self) :
        print("I can drive")
class Mother:
    def hobby(self) :
        print("I am a mom")
class Child(Father, Mother, Grandfather) :
    def talent(self) :
        print("We are Gen Z")
        
Obj1 = Child()
Obj1.skill()