class Test:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is created')
    def __del__(self) :
        print(f'{self.name} is created')
    def display(self) :
        print(f'I am {self.name}')
        
obj1 = Test("Object 1")
obj1.display()