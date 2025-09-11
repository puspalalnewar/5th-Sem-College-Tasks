class Calculator : 
    def multiply(self, *args):
        count = len(args)
        if count == 1:
            return args[0]*args[0]
        elif count == 2:
            return args[0]*args[1]
        elif count == 3 :
            return args[0]*args[1]*args[2]

cal_obj = Calculator()
print(cal_obj.multiply(2))
print(cal_obj.multiply(2, 3))
print(cal_obj.multiply(2, 3, 4))